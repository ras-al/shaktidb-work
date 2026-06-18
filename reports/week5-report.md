# Week 5 Report

## Name
Rasal Musthafa

## Project
ShaktiSOC: AI-Powered Security Operations Center using ShaktiDB

## Duration
16 June 2026 – 22 June 2026

---

## Work Completed

### 1. Database Schema Migration
* Executed a database schema migration in ShaktiDB (PostgreSQL) to support extended telemetry.
* Created `NetworkLogs` to track active TCP/UDP sockets and `FileLogs` to track system file modifications.

### 2. Network Telemetry Collector Development
* Developed `network_collector.py` using `psutil` to scan active network sockets.
* Implemented state-filtering logic to monitor `ESTABLISHED` connections and `LISTEN` states, enabling the detection of potential reverse shells and unauthorized data exfiltration.

### 3. File Integrity Monitoring (FIM) Collector
* Developed an asynchronous File Activity Collector (`file_collector.py`) using the `watchdog` library.
* Implemented event handlers to monitor critical directories (e.g., `/tmp`) for `CREATED`, `MODIFIED`, and `DELETED` actions in real-time.
* Successfully simulated and captured malicious script drops.

### 4. Backend REST API Development
* Designed and deployed the backend routing layer using the `Flask` framework (`api.py`).
* Implemented Cross-Origin Resource Sharing (CORS) to allow secure communication with future frontend interfaces.
* Developed modular API endpoints (`/api/logs/processes`, `/api/logs/network`, etc.) to securely execute SQL queries and serve ShaktiDB data as formatted JSON.


---

## Outcome
Successfully completed the Telemetry Collection Layer. The system now monitors processes, logins, network activity, and file integrity. Furthermore, a fully functional REST API was deployed, successfully bridging the ShaktiDB data repository with the web application layer.

---

## Plan for Week 6
* Integrate Scikit-Learn and Pandas.
* Develop the Threat Detection Engine.
* Train an Isolation Forest Machine Learning model on baseline telemetry.
* Implement real-time anomaly scoring and alert generation.

---

## Current Status
Database Integration: Completed  
Core Telemetry Collectors: Completed  
Advanced Telemetry (Network/FIM): Completed  
Backend API: Completed  
AI Threat Engine: Starting