# analytics/threat_detector.py

import os
import sys
import time
import logging
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class ThreatDetector:
    def __init__(self):
        self.db = DatabaseManager()
        self.model = IsolationForest(contamination=0.01, random_state=42)
        self.last_check_time = datetime.now() - timedelta(minutes=5)
        self.whitelist = ['chrome', 'firefox', 'code', 'gnome-shell', 'systemd', 'Xorg', 'psql']

    def prune_old_data(self):
        """Data Retention Policy: Deletes standard telemetry older than 7 days."""
        logging.info("Running automated database pruning...")
        queries = [
            "DELETE FROM ProcessLogs WHERE timestamp < NOW() - INTERVAL '7 days';",
            "DELETE FROM NetworkLogs WHERE timestamp < NOW() - INTERVAL '7 days';",
            "DELETE FROM FileLogs WHERE timestamp < NOW() - INTERVAL '7 days';"
        ]
        for q in queries:
            self.db.execute_query(q)
        logging.info("Database optimized. Old telemetry removed.")

    def fetch_training_data(self):
        query = "SELECT process_id, pid, process_name, cpu_usage, memory_usage, timestamp FROM ProcessLogs;"
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            return pd.DataFrame(data, columns=columns) if data else pd.DataFrame()
        except Exception as e:
            logging.error(f"Database error: {e}")
            self.db.connection.rollback()
            return pd.DataFrame()
        finally:
            if 'cursor' in locals():
                cursor.close()

    def check_correlation(self, new_anomalies):
        """
        CORRELATION ENGINE: Checks if a CPU spike happened at the exact same 
        time as suspicious network and file activity.
        """
        try:
            cursor = self.db.connection.cursor()
            
            # Check for simultaneous file changes
            cursor.execute("SELECT COUNT(*) FROM FileLogs WHERE timestamp > %s", (self.last_check_time,))
            recent_files = cursor.fetchone()[0]
            
            # Check for simultaneous network connections
            cursor.execute("SELECT COUNT(*) FROM NetworkLogs WHERE timestamp > %s", (self.last_check_time,))
            recent_networks = cursor.fetchone()[0]
            
            # If all three vectors happen at once, it's a massive red flag.
            if recent_files > 0 and recent_networks > 0:
                query = """
                    INSERT INTO Alerts (event_type, description, severity)
                    VALUES (%s, %s, %s);
                """
                for _, row in new_anomalies.iterrows():
                    desc = f"CORRELATED ATTACK: Unidentified process '{row['process_name']}' spiked CPU while {recent_files} files were modified and {recent_networks} network sockets opened."
                    self.db.execute_query(query, ("MALWARE_BEHAVIOR", desc, "CRITICAL"))
                return True
                
            return False
            
        except Exception as e:
            logging.error(f"Correlation Engine Error: {e}")
            self.db.connection.rollback()
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()

    def analyze_processes(self):
        df = self.fetch_training_data()
        
        if df.empty or len(df) < 20:
            return

        ml_df = df[~df['process_name'].isin(self.whitelist)]
        if ml_df.empty or len(ml_df) < 10:
            return 

        features = ml_df[['cpu_usage', 'memory_usage']]
        self.model.fit(features)
        
        ml_df = ml_df.copy()
        ml_df['anomaly_score'] = self.model.predict(features)

        anomalies = ml_df[ml_df['anomaly_score'] == -1]
        true_anomalies = anomalies[(anomalies['cpu_usage'] > 10.0) | (anomalies['memory_usage'] > 10.0)]
        new_anomalies = true_anomalies[true_anomalies['timestamp'] > self.last_check_time]
        
        if not new_anomalies.empty:
            logging.warning(f"Engine triggered! Analyzing {len(new_anomalies)} anomalies for threat correlation...")
            was_correlated = self.check_correlation(new_anomalies)
    
            if not was_correlated:
                self.generate_standard_alerts(new_anomalies)

        self.last_check_time = datetime.now()

    def generate_standard_alerts(self, anomalies_df):
        query = """
            INSERT INTO Alerts (event_type, description, severity)
            VALUES (%s, %s, %s);
        """
        for _, row in anomalies_df.iterrows():
            event_type = "UNAUTHORIZED_RESOURCE_SPIKE"
            desc = f"Unidentified process '{row['process_name']}' (PID: {row['pid']}) spiked to {row['cpu_usage']}% CPU."
            severity = "HIGH"
            self.db.execute_query(query, (event_type, desc, severity))

if __name__ == "__main__":
    logging.info("Starting Enterprise Correlation Engine...")
    detector = ThreatDetector()
    loops = 0
    try:
        while True:
            detector.analyze_processes()
            time.sleep(30)
            loops += 1
            if loops >= 120:
                detector.prune_old_data()
                loops = 0
                
    except KeyboardInterrupt:
        detector.db.close()