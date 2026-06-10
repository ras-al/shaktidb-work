# ShaktiSOC Architecture

## AI-Powered Security Operations Center using ShaktiDB

---

# System Overview

ShaktiSOC follows a layered architecture consisting of telemetry collection, database storage, analytics, and visualization.

The system collects events from Linux systems, stores them in ShaktiDB, analyzes them for suspicious activity, and presents insights through a monitoring dashboard.

---

# High-Level Architecture

```text
Linux System
│
├── Login Events
├── Process Events
├── Network Events
├── USB Events
└── File Events
        │
        ▼
Telemetry Collection Layer
        │
        ▼
ShaktiDB
        │
        ▼
Analytics & Threat Detection
        │
        ▼
Threat Scoring & Alerts
        │
        ▼
Dashboard & Reports
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

Analyzes stored telemetry data.

Functions:

* Behavioral Analysis
* Event Correlation
* Threat Scoring
* Anomaly Detection

Potential threat categories:

* Suspicious Logins
* Unusual Processes
* Network Anomalies
* Unauthorized Access Attempts

---

# 4. Dashboard Layer

Provides visibility into system activity.

Features:

* Event Monitoring
* Alert Dashboard
* Threat Statistics
* Security Reports

---

# Data Flow

1. Linux system generates events.
2. Collectors gather telemetry.
3. Events are stored in ShaktiDB.
4. Analytics engine processes data.
5. Threat scores are generated.
6. Alerts are created.
7. Dashboard displays results.

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
├── analytics/
│   ├── feature_extractor.py
│   ├── anomaly_detector.py
│   ├── threat_scorer.py
│   └── alert_engine.py
├── dashboard/
│   ├── app.py
│   ├── api.py
│   └── templates/
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