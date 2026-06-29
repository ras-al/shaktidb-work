import os
import sys
from flask import Flask, jsonify
from flask_cors import CORS
import logging

# Ensure we can import from the db folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.connection import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)
# Enable CORS so our future frontend can talk to this API
CORS(app)

def fetch_data_as_dict(query):
    """
    Helper function to execute a SELECT query and return the 
    results as a list of dictionaries (which easily converts to JSON).
    """
    db = DatabaseManager()
    if not db.connection:
        return {"error": "Database connection failed"}
        
    try:
        cursor = db.connection.cursor()
        cursor.execute(query)
        
        # Get column names from the cursor description
        columns = [desc[0] for desc in cursor.description]
        
        # Zip column names with row values
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
            
        return results
    except Exception as e:
        logging.error(f"Failed to fetch data: {e}")
        return {"error": str(e)}
    finally:
        if 'cursor' in locals():
            cursor.close()
        db.close()

# --- API ENDPOINTS ---

@app.route('/api/status', methods=['GET'])
def get_status():
    """Simple endpoint to check if the API is running."""
    return jsonify({"status": "online", "service": "ShaktiSOC API"})

@app.route('/api/logs/processes', methods=['GET'])
def get_process_logs():
    # Fetch the 50 most recent high-usage process events
    query = "SELECT * FROM ProcessLogs ORDER BY timestamp DESC LIMIT 50;"
    return jsonify(fetch_data_as_dict(query))

@app.route('/api/logs/logins', methods=['GET'])
def get_login_logs():
    # Fetch the 50 most recent SSH login events
    query = "SELECT * FROM LoginLogs ORDER BY timestamp DESC LIMIT 50;"
    return jsonify(fetch_data_as_dict(query))

@app.route('/api/logs/network', methods=['GET'])
def get_network_logs():
    # Fetch the 50 most recent network connections
    query = "SELECT * FROM NetworkLogs ORDER BY timestamp DESC LIMIT 50;"
    return jsonify(fetch_data_as_dict(query))

@app.route('/api/logs/files', methods=['GET'])
def get_file_logs():
    # Fetch the 50 most recent file system changes
    query = "SELECT * FROM FileLogs ORDER BY timestamp DESC LIMIT 50;"
    return jsonify(fetch_data_as_dict(query))
@app.route('/api/logs/alerts', methods=['GET'])

def get_alerts():
    # Fetch the 50 most recent AI-generated security alerts
    query = "SELECT * FROM Alerts ORDER BY timestamp DESC LIMIT 50;"
    return jsonify(fetch_data_as_dict(query))

if __name__ == '__main__':
    # Run the Flask server on port 5000
    logging.info("Starting ShaktiSOC API Server...")
    app.run(host='0.0.0.0', port=5000, debug=True)