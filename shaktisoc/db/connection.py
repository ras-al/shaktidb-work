import psycopg2
from psycopg2 import Error
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class DatabaseManager:
    def __init__(self):
        """
        Initializes the connection to ShaktiDB (PostgreSQL).
        It securely fetches credentials from Linux Environment Variables.
        """
        # We use os.getenv to pull secure info from the OS
        self.db_name = os.getenv("SHAKTI_DB_NAME", "shaktisoc")
        self.db_user = os.getenv("SHAKTI_DB_USER", "postgres")
        self.db_password = os.getenv("SHAKTI_DB_PASSWORD", "6618618")
        self.db_host = os.getenv("SHAKTI_DB_HOST", "127.0.0.1")
        self.db_port = os.getenv("SHAKTI_DB_PORT", "5432")

        self.connection = None
        self.connect()

    def connect(self):
        """Establishes a connection to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            logging.info("Successfully connected to ShaktiDB (PostgreSQL).")
        except Error as e:
            logging.error(f"Error connecting to PostgreSQL: {e}")

    def execute_query(self, query, parameters=None):
        """Executes INSERT/UPDATE/DELETE queries securely."""
        if self.connection is None:
            logging.error("No database connection.")
            return False
            
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, parameters)
            self.connection.commit()
            return True
        except Error as e:
            logging.error(f"Query Execution Failed: {e}")
            self.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def close(self):
        """Closes the connection pool."""
        if self.connection:
            self.connection.close()
            logging.info("PostgreSQL connection closed.")