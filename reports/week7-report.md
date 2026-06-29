# Week 7 Report

## Name
Rasal Musthafa

## Project
ShaktiSOC: AI-Powered Security Operations Center using ShaktiDB

## Duration
30 June 2026 – 06 July 2026

---

## Work Completed

### 1. Enterprise Web Dashboard Development
* Bootstrapped a decoupled frontend application using React.js and Vite.
* Transitioned from standard CSS to **Tailwind CSS** to build a responsive, production-grade UI with advanced grid layouts, dark-mode aesthetics, and dynamic status indicators.
* Integrated `recharts` for live CPU telemetry visualization and `lucide-react` for scalable UI iconography.

### 2. Comprehensive REST API Integration
* Upgraded the Flask backend API to include the `/api/logs/alerts` endpoint.
* Implemented asynchronous data fetching (`axios`) with 5-second polling intervals to pull live telemetry across all modules: CPU, Network Sockets, File Integrity (FIM), SSH Authentication, and ML Alerts.
* Successfully mapped raw PostgreSQL JSON responses into dynamic React state variables.

### 3. AI Threat Engine Refinement (Alert Fatigue Mitigation)
* Addressed real-world "Alert Fatigue" by upgrading the Isolation Forest model to be context-aware.
* Implemented process **Whitelisting** (e.g., ignoring standard browser spikes from Chrome/Firefox) to eliminate false positives.
* Introduced **Hard Thresholds** (requiring anomalies to also exceed 10% CPU/Memory) and lowered the contamination rate to 1% to ensure only high-fidelity, actionable threats generate alerts.

### 4. Database Maintenance & Final End-to-End Validation
* Executed a "Clean Slate" protocol (`TRUNCATE ... RESTART IDENTITY`) on ShaktiDB to wipe developmental test data and reset database indexes for production use.
* Conducted final end-to-end integration testing: Simulated CPU stress tests, unauthorized SSH logins, and malicious file drops, successfully verifying their immediate appearance on the React dashboard.


---

## Outcome
The ShaktiSOC project is officially complete. The system successfully operates as a production-ready, full-stack cybersecurity monitoring platform. It actively ingests multi-vector OS telemetry, stores it efficiently in ShaktiDB, analyzes it via a context-aware machine learning model, and visualizes high-fidelity alerts on a live, interactive React dashboard.

---

## Current Status
Database Integration: Completed  
Core Telemetry Collectors: Completed  
Advanced Telemetry (Network/FIM): Completed  
Backend API: Completed  
AI Threat Engine: Completed (Production Tuned)  
Web Dashboard: Completed (Tailwind UI)  
Project: Successfully Delivered