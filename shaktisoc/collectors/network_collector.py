import os
import sys
import time
import psutil
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def collect_network_connections():
    """
    Scans for active ESTABLISHED network connections.
    """
    db = DatabaseManager()
    logging.info("Scanning active network connections...")

    # net_connections('inet') filters for IPv4 and IPv6 connections only
    for conn in psutil.net_connections(kind='inet'):
        if conn.status in ['ESTABLISHED', 'LISTEN']:
            protocol = 'TCP' if conn.type == 1 else 'UDP'
            
            local_ip = conn.laddr.ip if conn.laddr else 'unknown'
            local_port = conn.laddr.port if conn.laddr else 0
            
            remote_ip = conn.raddr.ip if conn.raddr else 'none'
            remote_port = conn.raddr.port if conn.raddr else 0

            if local_ip == '127.0.0.1' and remote_ip == '127.0.0.1':
                continue

            query = """
                INSERT INTO NetworkLogs (local_ip, local_port, remote_ip, remote_port, protocol, status)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            db.execute_query(query, (local_ip, local_port, remote_ip, remote_port, protocol, conn.status))
            logging.info(f"Logged Network Event: {protocol} {local_ip}:{local_port} -> {remote_ip}:{remote_port} [{conn.status}]")

    db.close()

if __name__ == "__main__":
    logging.info("ShaktiSOC Network Daemon started. Press Ctrl+C to exit.")
    try:
        while True:
            collect_network_connections()
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("Network Daemon stopped manually.")