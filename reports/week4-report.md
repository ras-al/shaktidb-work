# Week 4 Report

## Name
Rasal Musthafa

## Project
ShaktiSOC: AI-Powered Security Operations Center using ShaktiDB

## Duration
09 June 2026 – 15 June 2026

---

## Work Completed

### 1. Database Schema Design and Integration
* Designed the relational database schema for ShaktiSOC, optimized for time-series security events.
* Created tables in ShaktiDB (PostgreSQL) including `Users`, `LoginLogs`, `ProcessLogs`, and `Alerts`.
* Developed a secure Python database connector (`connection.py`) utilizing `psycopg2` and environment variables to prevent hardcoded credentials.

### 2. Process Telemetry Collector Development
* Developed a continuous polling daemon (`process_collector.py`) using Python's `psutil` library.
* Implemented edge-filtering logic to only log processes exceeding specific CPU/Memory thresholds, effectively preventing database bloat.
* Successfully ingested live process metadata (PID, process name, resource usage) into ShaktiDB.

### 3. Login Telemetry Collector Development
* Developed an event-driven daemon (`login_collector.py`) to monitor SSH access attempts.
* Utilized Linux log tailing techniques on `/var/log/auth.log`.
* Implemented Regular Expressions (Regex) to parse unstructured log lines and extract structured data (username, IP address, success/failure status).
* Established successful database ingestion for all SSH login events.

### 4. System Administration & Troubleshooting
* **Environment Gap Resolution:** Resolved a Python module dependency issue where the root user (`sudo`) could not access the `psycopg2` library installed in the local user environment. Fixed this by managing Python packages globally via `apt`.
* **SSH Server Configuration:** Configured the Ubuntu environment to accept and log incoming SSH connections by installing and enabling `openssh-server`, allowing the system to accurately simulate and record brute-force attack telemetry.

---

## Skills Learned
* PostgreSQL Relational Schema Design.
* Python Database Integration (`psycopg2`).
* Live OS Telemetry Extraction (`psutil`).
* Advanced Text Parsing and Pattern Matching using Regular Expressions (Regex).
* Linux System Administration (Service management, `sudo` environment variables, SSH configuration).

---

## Outcome
Successfully transitioned from architectural design to active development. The system is now actively collecting live OS telemetry and successfully storing time-series security data within ShaktiDB. Real-world troubleshooting was successfully performed to ensure the data ingestion pipeline is fully operational.

---

## Plan for Week 5
* Develop remaining telemetry collectors (Network and File Activity).
* Initialize the Flask backend.
* Create REST API endpoints to query database logs.
* Begin preparing data for the Machine Learning threat detection engine.

---

## Current Status
Database Integration: Completed  
Core Telemetry Collectors: Completed  
System Configuration: Completed  
Backend API: Starting