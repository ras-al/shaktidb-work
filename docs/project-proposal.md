# ShaktiSOC

## AI-Powered Security Operations Center using ShaktiDB

### Author

Rasal Musthafa

---

# Abstract

ShaktiSOC is a cybersecurity monitoring platform designed to collect Linux system telemetry, store security events in ShaktiDB, and analyze system activities using machine learning-based anomaly detection techniques.

The system continuously monitors user logins, running processes, network activity, USB events, and file system operations. Collected telemetry is stored in ShaktiDB and analyzed to identify suspicious behavior and potential security threats.

The project aims to demonstrate the use of ShaktiDB for handling continuous event ingestion, analytical queries, and security monitoring workloads.

---

# Problem Statement

Traditional security monitoring systems rely on predefined rules to detect threats. Such systems often fail to identify new or evolving attack patterns.

A centralized platform is required that can:

* Collect system telemetry
* Store large volumes of security data
* Analyze behavioral patterns
* Detect anomalies
* Generate security alerts

---

# Objectives

The objectives of ShaktiSOC are:

1. Collect Linux security telemetry.
2. Store security events in ShaktiDB.
3. Analyze system behavior.
4. Detect suspicious activities.
5. Generate threat alerts.
6. Provide security analytics and reporting.
7. Evaluate ShaktiDB under real-world workloads.

---

# Proposed Modules

## Telemetry Collection

Collects:

* Login Activity
* Process Activity
* Network Activity
* USB Events
* File Activity

---

## Database Layer

Stores collected telemetry in ShaktiDB.

Proposed tables:

* Users
* LoginLogs
* ProcessLogs
* NetworkLogs
* USBLogs
* FileLogs
* Alerts

---

## Analytics & Threat Detection

Analyzes collected telemetry and identifies unusual behavior.

Planned techniques:

* Behavioral Analysis
* Threat Scoring
* Anomaly Detection

---

## Dashboard

Provides:

* Event Monitoring
* Alert Monitoring
* Threat Statistics
* Security Reports

---

# Technology Stack

Database:

* ShaktiDB

Backend:

* Python

Machine Learning:

* Scikit-Learn
* Pandas
* NumPy

Dashboard:

* Flask

Operating System:

* Ubuntu 22.04 LTS

Version Control:

* Git
* GitHub

---

# Expected Outcomes

Upon completion, the system should:

* Continuously collect security telemetry.
* Store telemetry efficiently in ShaktiDB.
* Generate security alerts.
* Provide monitoring and reporting capabilities.
* Demonstrate database-driven cybersecurity analytics.

---

# Future Scope

Future enhancements may include:

* Advanced AI Models
* Threat Intelligence Integration
* Automated Incident Response
* Multi-Host Monitoring
* AI-Assisted Security Analysis

---

# Conclusion

ShaktiSOC combines Linux telemetry collection, database management, and security analytics into a unified platform. The project serves as a practical application for evaluating ShaktiDB while exploring cybersecurity monitoring concepts.
