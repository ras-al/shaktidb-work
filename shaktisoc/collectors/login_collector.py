import os
import sys
import re
import logging
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def tail_auth_log():
    """
    Tails the Ubuntu /var/log/auth.log file continuously.
    """
    db = DatabaseManager()
    log_file = '/var/log/auth.log'
    
    # Regex patterns for SSH logins
    # The (\w+) captures the username, and ([\d\.]+) captures the IP address
    failed_pattern = re.compile(r"Failed \w+ for (?:invalid user )?(\w+) from ([\d\.]+)")
    accepted_pattern = re.compile(r"Accepted \w+ for (\w+) from ([\d\.]+)")

    if not os.path.exists(log_file):
        logging.error(f"Log file {log_file} not found. Ensure you are on Ubuntu.")
        return

    logging.info(f"Starting Login Telemetry Collector. Tailing {log_file}...")
    
    # Using subprocess to run 'tail -F' which safely handles log file rotations
    process = subprocess.Popen(['tail', '-F', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        # iter() allows us to read the output line-by-line continuously
        for line in iter(process.stdout.readline, b''):
            line = line.decode('utf-8').strip()
            
            # Check for failed logins
            failed_match = failed_pattern.search(line)
            if failed_match:
                username = failed_match.group(1)
                ip_address = failed_match.group(2)
                log_event(db, username, 'FAILED', ip_address)
                continue

            # Check for successful logins
            accepted_match = accepted_pattern.search(line)
            if accepted_match:
                username = accepted_match.group(1)
                ip_address = accepted_match.group(2)
                log_event(db, username, 'SUCCESS', ip_address)

    except KeyboardInterrupt:
        logging.info("Login Collector stopped manually.")
    finally:
        process.terminate()
        db.close()

def log_event(db, username, status, ip_address):
    """Inserts the parsed login event into ShaktiDB."""
    query = """
        INSERT INTO LoginLogs (username, status, source_ip)
        VALUES (%s, %s, %s);
    """
    db.execute_query(query, (username, status, ip_address))
    logging.info(f"Logged SSH Event: {status} login for '{username}' from {ip_address}")

if __name__ == "__main__":
    tail_auth_log()