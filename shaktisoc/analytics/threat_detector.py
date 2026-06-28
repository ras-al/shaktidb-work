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
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.last_check_time = datetime.now() - timedelta(minutes=5)

    def fetch_training_data(self):
        query = "SELECT process_id, pid, process_name, cpu_usage, memory_usage, timestamp FROM ProcessLogs;"
        
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            
            if not data:
                return pd.DataFrame()
                
            return pd.DataFrame(data, columns=columns)
        except Exception as e:
            logging.error(f"Failed to fetch training data: {e}")
            self.db.connection.rollback()
            return pd.DataFrame()
        finally:
            if 'cursor' in locals():
                cursor.close()

    def analyze_processes(self):
        df = self.fetch_training_data()
        
        if df.empty or len(df) < 20:
            logging.warning("Not enough data to train the AI. Let the collector run longer.")
            return

        features = df[['cpu_usage', 'memory_usage']]

        logging.info("Training Isolation Forest on system baseline...")
        self.model.fit(features)
        
        df['anomaly_score'] = self.model.predict(features)

        anomalies = df[df['anomaly_score'] == -1]
        new_anomalies = anomalies[anomalies['timestamp'] > self.last_check_time]
        
        if not new_anomalies.empty:
            logging.info(f"Detected {len(new_anomalies)} NEW anomalous events! Generating alerts...")
            self.generate_alerts(new_anomalies)
        else:
            logging.info("System is secure. No new anomalies detected.")

        self.last_check_time = datetime.now()

    def generate_alerts(self, anomalies_df):
        query = """
            INSERT INTO Alerts (event_type, description, severity)
            VALUES (%s, %s, %s);
        """
        for index, row in anomalies_df.iterrows():
            event_type = "PROCESS_ANOMALY"
            desc = f"Suspicious activity detected: {row['process_name']} (PID: {row['pid']}) using {row['cpu_usage']}% CPU and {row['memory_usage']}% Memory."
            severity = "CRITICAL" if row['cpu_usage'] > 50.0 or row['memory_usage'] > 50.0 else "HIGH"
            
            self.db.execute_query(query, (event_type, desc, severity))

    def close(self):
        self.db.close()

if __name__ == "__main__":
    logging.info("Starting AI Threat Engine...")
    detector = ThreatDetector()
    
    try:
        while True:
            detector.analyze_processes()
            time.sleep(30)
    except KeyboardInterrupt:
        logging.info("AI Threat Engine stopped manually.")
    finally:
        detector.close()