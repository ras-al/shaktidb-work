import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class SecurityFileHandler(FileSystemEventHandler):
    """
    This is our Asynchronous Event Handler.
    It automatically triggers these methods when the OS detects a change.
    """
    def __init__(self):
        self.db = DatabaseManager()

    def log_to_db(self, file_path, action):
        query = """
            INSERT INTO FileLogs (file_path, action_type)
            VALUES (%s, %s);
        """
        self.db.execute_query(query, (file_path, action))
        logging.info(f"File Event: {action} -> {file_path}")

    def on_created(self, event):
        if not event.is_directory:
            self.log_to_db(event.src_path, 'CREATED')

    # Called when a file is modified
    def on_modified(self, event):
        if not event.is_directory:
            self.log_to_db(event.src_path, 'MODIFIED')

    # Called when a file is deleted
    def on_deleted(self, event):
        if not event.is_directory:
            self.log_to_db(event.src_path, 'DELETED')

def start_file_monitor(path_to_watch):
    logging.info(f"Starting File Telemetry Collector on directory: {path_to_watch}")
    
    # 1. Create our custom event handler
    event_handler = SecurityFileHandler()
    
    # 2. Create an Observer (the engine that talks to the Linux kernel)
    observer = Observer()
    
    # 3. Tell the Observer to watch the path recursively (all subfolders)
    observer.schedule(event_handler, path_to_watch, recursive=True)
    
    # 4. Start the background thread
    observer.start()
    
    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        logging.info("File Collector stopped manually.")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    # For testing, we will watch /tmp because it is safe and malware loves to hide there.
    TARGET_DIR = "/tmp" 
    
    if os.path.exists(TARGET_DIR):
        start_file_monitor(TARGET_DIR)
    else:
        logging.error(f"Directory {TARGET_DIR} does not exist.")