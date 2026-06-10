import os
import sys
import time
import psutil
import logging

# To look for the 'db' folder in the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def collect_high_usage_processes(cpu_threshold=5.0, memory_threshold=5.0):
    """
    Scans running processes and records any that exceed CPU or Memory thresholds.
    """
    db = DatabaseManager()
    logging.info("Starting process telemetry collection snapshot...")

    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username']):
        try:
            proc_info = proc.info
            pid = proc_info['pid']
            name = proc_info['name']
            cpu = proc_info['cpu_percent'] if proc_info['cpu_percent'] is not None else 0.0
            memory = proc_info['memory_percent'] if proc_info['memory_percent'] is not None else 0.0
            username = proc_info['username'] if proc_info['username'] is not None else 'unknown'

            # Filter out idle background processes to avoid filling the DB with useless noise
            if cpu > cpu_threshold or memory > memory_threshold:
                query = """
                    INSERT INTO ProcessLogs (pid, process_name, cpu_usage, memory_usage, username)
                    VALUES (%s, %s, %s, %s, %s);
                """
                db.execute_query(query, (pid, name, cpu, memory, username))
                logging.info(f"Logged suspicious process: {name} (PID: {pid}) - CPU: {cpu}%, MEM: {memory:.2f}%")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    db.close()

if __name__ == "__main__":
    logging.info("ShaktiSOC Process Daemon started. Press Ctrl+C to exit.")
    try:
        while True:
            # Collect data
            collect_high_usage_processes(cpu_threshold=2.0, memory_threshold=2.0)
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Process Daemon stopped manually.")