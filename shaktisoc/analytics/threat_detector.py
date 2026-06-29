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

    def analyze_processes(self):
        df = self.fetch_training_data()
        
        if df.empty or len(df) < 20:
            return

        # 1. Filter out known trusted applications before ML training
        ml_df = df[~df['process_name'].isin(self.whitelist)]
        
        if ml_df.empty or len(ml_df) < 10:
            return

        features = ml_df[['cpu_usage', 'memory_usage']]
        self.model.fit(features)
        
        ml_df = ml_df.copy()
        ml_df['anomaly_score'] = self.model.predict(features)

        # 2. Extract Anomalies
        anomalies = ml_df[ml_df['anomaly_score'] == -1]
        
        # 3. PRODUCTION TUNING: Apply a Hard Threshold. 
        true_anomalies = anomalies[(anomalies['cpu_usage'] > 10.0) | (anomalies['memory_usage'] > 10.0)]
        
        # 4. Time filtering
        new_anomalies = true_anomalies[true_anomalies['timestamp'] > self.last_check_time]
        
        if not new_anomalies.empty:
            logging.warning(f"CRITICAL: Detected {len(new_anomalies)} unverified anomalous events!")
            self.generate_alerts(new_anomalies)

        self.last_check_time = datetime.now()

    def generate_alerts(self, anomalies_df):
        query = """
            INSERT INTO Alerts (event_type, description, severity)
            VALUES (%s, %s, %s);
        """
        for _, row in anomalies_df.iterrows():
            event_type = "UNAUTHORIZED_RESOURCE_SPIKE"
            desc = f"Unidentified process '{row['process_name']}' (PID: {row['pid']}) spiked to {row['cpu_usage']}% CPU."
            severity = "CRITICAL" if row['cpu_usage'] > 40.0 else "HIGH"
            self.db.execute_query(query, (event_type, desc, severity))

if __name__ == "__main__":
    logging.info("Starting Production AI Threat Engine...")
    detector = ThreatDetector()
    try:
        while True:
            detector.analyze_processes()
            time.sleep(30)
    except KeyboardInterrupt:
        detector.db.close()