# ShaktiSOC Architecture

## AI-Powered Security Operations Center using ShaktiDB

---

# System Overview

ShaktiSOC follows a layered architecture consisting of telemetry collection, database storage, analytics, and visualization.

The system collects events from Linux systems, stores them in ShaktiDB, analyzes them for suspicious activity, and presents insights through a monitoring dashboard.

---

# High-Level Architecture

```text
Linux System (Endpoint)
│
├── Login Events
├── Process Events
├── Network Events
├── USB Events
└── File Events
        │
        ▼
Telemetry Collection Layer (Python Daemons)
        │
        ▼
ShaktiDB
        │
        ▼
Backend API & Analytics Layer (Flask / FastAPI)
│       ├── Threat Detection Engine (Scikit-Learn / Isolation Forest)
│       ├── Threat Scoring & Alerts
│       └── Data Aggregation
        │
        ▼
RESTful JSON APIs
        │
        ▼
Web-Based Analytics Dashboard (React.js / Next.js)
        ├── Real-time Threat Map & Graphs
        ├── Security Event Logs
        └── Active Alerts Panel
```

---

# Component Description

## 1. Telemetry Collection Layer

Responsible for gathering events from the Linux operating system.

### Login Collector

Collects:

* Username
* Login Status
* Login Time
* Source IP

---

### Process Collector

Collects:

* Process Name
* CPU Usage
* Memory Usage
* User

---

### Network Collector

Collects:

* Source IP
* Destination IP
* Port
* Protocol

---

### USB Collector

Collects:

* Device Name
* Vendor Information
* Timestamp

---

### File Activity Collector

Collects:

* File Name
* Action Type
* User
* Timestamp

---

# 2. Database Layer

ShaktiDB serves as the central event repository.

## Planned Tables

| Table       | Purpose                |
| ----------- | ---------------------- |
| Users       | User information       |
| LoginLogs   | Login activities       |
| ProcessLogs | Process events         |
| NetworkLogs | Network events         |
| USBLogs     | USB activities         |
| FileLogs    | File system activities |
| Alerts      | Security alerts        |

---

# 3. Analytics & Threat Detection Layer

Acts as the API and ML execution layer for stored telemetry data.

Functions:

* Data Aggregation
* Behavioral Analysis
* Event Correlation
* Threat Scoring
* Anomaly Detection

Execution stack:

* Flask or FastAPI
* Scikit-Learn Isolation Forest

Potential threat categories:

* Suspicious Logins
* Unusual Processes
* Network Anomalies
* Unauthorized Access Attempts

---

# 4. Dashboard Layer

Provides web-based visibility into system activity via RESTful JSON APIs.

Features:

* Real-time Threat Map and Graphs
* Security Event Logs
* Active Alerts Panel
* Threat Statistics
* Security Reports

---

# Data Flow

1. Linux system generates events.
2. Collectors gather telemetry.
3. Events are stored in ShaktiDB.
4. Backend API and analytics layer aggregates and analyzes data.
5. Threat scores and alerts are generated.
6. RESTful JSON APIs expose results.
7. Web dashboard visualizes security activity.

---

# Repository Structure

```text
shaktisoc/
├── db/
│   ├── schema.sql
│   └── connection.py
├── collectors/
│   ├── login_collector.py
│   ├── process_collector.py
│   ├── network_collector.py
│   ├── usb_collector.py
│   ├── file_collector.py
│   └── runner.py
├── backend/
│   ├── api.py
│   ├── analytics.py
│   ├── threat_detection.py
│   └── alerts.py
├── frontend/
│   ├── src/
│   └── public/
├── scripts/
│   └── start_shaktisoc.sh
└── requirements.txt
```

---

# Future Enhancements

* Machine Learning Based Detection
* Automated Response Actions
* Multi-System Monitoring
* Threat Intelligence Integration
* AI-Assisted Incident Analysis

---