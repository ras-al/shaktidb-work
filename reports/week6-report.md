# Week 6 Report

## Name
Rasal Musthafa

## Project
ShaktiSOC: AI-Powered Security Operations Center using ShaktiDB

## Duration
23 June 2026 – 29 June 2026

---

## Work Completed

### 1. AI Threat Engine Architecture
* Designed and implemented the `ThreatDetector` module to provide real-time behavioral analysis of system telemetry.
* Integrated the `pandas` library to transform raw PostgreSQL time-series logs into structured mathematical data frames suitable for machine learning.

### 2. Unsupervised Machine Learning Integration
* Implemented the **Isolation Forest** algorithm using `scikit-learn` for anomaly detection.
* Configured the model to dynamically train on the host system's baseline CPU and Memory telemetry, bypassing the need for static, pre-labeled attack datasets.
* Successfully detected high-resource outlier processes (simulated spikes) and isolated them from standard background noise.

### 3. Real-Time Alert Generation & Time-Series Filtering
* Developed an automated alerting mechanism that writes flagged anomalies directly into the ShaktiDB `Alerts` table.
* Handled time-series data duplication bugs by engineering a time-window filter (`last_check_time`), ensuring the AI only generates alerts for *new* anomalies rather than endlessly reprocessing historical data.
* Resolved `psycopg2` transaction block errors by properly implementing connection rollbacks during failed database fetches.

---

## Outcome
The analytic brain of ShaktiSOC is officially operational. The system no longer just collects data; it actively analyzes it, understands the baseline, and automatically generates high-priority alerts when anomalous system behavior occurs.

---

## Plan for Week 7 (Final Week)
* Develop the React.js / Next.js web frontend.
* Connect the frontend to the Flask REST API.
* Build an interactive monitoring dashboard with real-time charts and an Active Alerts panel.
* Conduct end-to-end system testing and finalize project documentation.

---

## Current Status
Database Integration: Completed  
Core Telemetry Collectors: Completed  
Backend API: Completed  
AI Threat Engine: Completed  
Web Dashboard: Starting