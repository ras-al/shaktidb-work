# ShakthiSOC

## AI-Powered Linux Security Monitoring and Threat Detection Platform using ShaktiDB

### Author

Rasal Musthafa

### Technology Stack

* ShaktiDB
* Python
* Flask
* Scikit-Learn
* Ubuntu Linux
* GitHub

---

# 1. Abstract

ShakthiSOC is an AI-powered cybersecurity monitoring platform designed to collect Linux system telemetry, store security events in ShaktiDB, and detect malicious activities using machine learning-based anomaly detection.

The system continuously monitors login activity, running processes, network connections, USB device usage, and file system events. These events are stored inside ShaktiDB and analyzed by an Artificial Intelligence engine to identify suspicious behavior, security threats, and abnormal system activities.

Unlike traditional security monitoring systems that rely on fixed rules, ShakthiSOC learns normal system behavior and automatically identifies anomalies through unsupervised machine learning techniques.

The project demonstrates practical applications of databases, cybersecurity, artificial intelligence, and Linux systems engineering.

---

# 2. Problem Statement

Most traditional security systems rely on predefined rules such as:

* More than 5 failed logins
* More than 100 network requests
* Blacklisted process execution

Modern attackers can bypass these static rules using slow and stealthy attack methods.

Examples include:

* Slow brute-force attacks
* Credential stuffing attacks
* Insider threats
* Unauthorized process execution
* Advanced Persistent Threats (APT)

A more intelligent solution is required that can learn normal behavior and automatically identify suspicious activities.

---

# 3. Project Objectives

The objectives of ShakthiSOC are:

1. Monitor Linux system activities in real time.
2. Store large-scale security telemetry using ShaktiDB.
3. Detect abnormal system behavior using Artificial Intelligence.
4. Generate security alerts based on threat scores.
5. Provide a centralized monitoring dashboard.
6. Evaluate ShaktiDB performance under continuous log ingestion.
7. Demonstrate AI-assisted cybersecurity monitoring.

---

# 4. System Architecture

Linux System
↓
Telemetry Collection Layer
↓
ShaktiDB Database
↓
AI Threat Detection Engine
↓
Threat Scoring Module
↓
Security Dashboard
↓
Alert Generation

---

# 5. Modules

## Module 1: Telemetry Collection

The system continuously collects data from Linux operating system components.

### Login Monitoring

Collected Information:

* Username
* Login Time
* Login Status
* Source IP

Source:

* journalctl
* auth.log

---

### Process Monitoring

Collected Information:

* Process Name
* CPU Usage
* Memory Usage
* User

Source:

* ps
* top

---

### Network Monitoring

Collected Information:

* Source IP
* Destination IP
* Port Number
* Protocol

Source:

* ss
* netstat

---

### USB Device Monitoring

Collected Information:

* Device Name
* Vendor Information
* Timestamp

Source:

* lsusb

---

### File Activity Monitoring

Collected Information:

* File Name
* Action Type
* User
* Timestamp

Actions:

* Create
* Modify
* Delete
* Read

---

# 6. Database Design

## Users

Stores registered system users.

Attributes:

* User ID
* Username
* Role

---

## LoginLogs

Stores login-related activities.

Attributes:

* Log ID
* Username
* IP Address
* Status
* Timestamp

---

## ProcessLogs

Stores process execution information.

Attributes:

* Process Name
* CPU Usage
* Memory Usage
* User
* Timestamp

---

## NetworkLogs

Stores network activities.

Attributes:

* Source IP
* Destination IP
* Port
* Protocol
* Timestamp

---

## USBLogs

Stores USB device activities.

Attributes:

* Device Name
* Vendor ID
* Timestamp

---

## FileLogs

Stores file access activities.

Attributes:

* Filename
* Action
* User
* Timestamp

---

## Alerts

Stores security alerts.

Attributes:

* Severity
* Threat Type
* Description
* Confidence Score
* Timestamp

---

# 7. Artificial Intelligence Engine

The AI engine analyzes collected telemetry and detects abnormal behavior.

## Algorithm

Isolation Forest

Reason for Selection:

* Unsupervised Learning
* No labeled dataset required
* Efficient anomaly detection
* Lightweight implementation

---

## Feature Extraction

Login Features:

* Login Hour
* Failed Login Count
* Login Frequency

Process Features:

* CPU Usage
* Memory Usage
* Process Category

Network Features:

* Connection Count
* Port Activity
* Protocol Distribution

File Features:

* Number of Modifications
* Number of Deletions

---

# 8. Threat Detection Capabilities

The system can identify:

### Brute Force Attacks

Multiple failed login attempts.

---

### Credential Stuffing

One source attempting multiple user accounts.

---

### Port Scanning

Rapid access to multiple ports.

---

### Suspicious Login Times

User behavior outside normal operating hours.

---

### Unauthorized Process Execution

Execution of uncommon or suspicious tools.

Examples:

* nmap
* hydra
* masscan

---

### Insider Threats

Unusual access to files or resources.

---

### Ransomware Indicators

Mass deletion or modification of files.

---

# 9. Threat Scoring System

Every event receives a threat score.

Example:

Normal Login:
5

Failed Login:
20

USB Insertion:
25

Port Scan:
70

Mass File Deletion:
95

Threat Levels:

0 – 30 : Low

31 – 60 : Medium

61 – 80 : High

81 – 100 : Critical

---

# 10. Security Dashboard

The dashboard provides real-time visibility into system activities.

Features:

### Event Statistics

* Total Events
* Total Alerts
* Critical Alerts

### Alert Viewer

Displays:

* Severity
* Threat Type
* Confidence Score

### Graphical Analytics

* Login Trends
* Attack Trends
* Threat Distribution

### Event Explorer

Allows searching and filtering logs.

---

# 11. Report Generation

The platform generates:

### Daily Security Report

Includes:

* Total Events
* Alerts Generated
* Threat Summary

### Weekly Security Report

Includes:

* Attack Statistics
* Top Threat Sources

### Monthly Report

Includes:

* Security Overview
* Risk Assessment

Export Formats:

* PDF
* CSV

---

# 12. Expected Outcomes

Upon completion, ShakthiSOC will:

* Collect Linux security telemetry
* Store data efficiently using ShaktiDB
* Detect anomalous behavior using AI
* Generate automated security alerts
* Provide centralized monitoring capabilities
* Demonstrate practical database and cybersecurity skills

---

# 13. Future Scope

## Phase 2: Advanced AI Models

Upgrade from Isolation Forest to:

* Autoencoders
* LSTM Networks
* Deep Learning Models

for more accurate behavioral analysis.

---

## Phase 3: Security Orchestration and Automated Response (SOAR)

Automatically respond to attacks by:

* Blocking malicious IP addresses
* Terminating suspicious processes
* Isolating compromised systems

---

## Phase 4: Cryptographic Log Integrity

Implement blockchain-inspired log chaining to prevent attackers from modifying stored evidence.

Benefits:

* Tamper-proof audit trail
* Improved forensic reliability

---

## Phase 5: AI Security Analyst

Integrate a Large Language Model (LLM) capable of:

* Explaining detected threats
* Generating incident summaries
* Suggesting mitigation actions

Example:

"Potential brute-force attack detected from IP 192.168.1.10. Recommend temporary blocking and account review."

---

## Phase 6: Multi-Host Enterprise Monitoring

Expand ShakthiSOC to monitor:

* Multiple Linux Servers
* Cloud Infrastructure
* Containerized Environments

through centralized ShaktiDB storage.

---

## Phase 7: Threat Intelligence Integration

Integrate external threat intelligence feeds.

Capabilities:

* Malicious IP detection
* Malicious domain detection
* Known malware signature identification

---

# 14. Project Timeline

Week 1:

* ShaktiDB Installation
* Environment Setup
* Database Schema Design

Week 2:

* Telemetry Collection Development

Week 3:

* Database Integration
* Data Storage Layer

Week 4:

* Dashboard Development

Week 5:

* AI Model Development
* Threat Detection Engine

Week 6:

* Testing
* Documentation
* Bug Reporting
* Final Presentation

---

# 15. Conclusion

ShakthiSOC combines cybersecurity, artificial intelligence, Linux systems engineering, and database technologies into a unified security monitoring platform. The project leverages ShaktiDB as its central storage engine while applying machine learning techniques to identify threats and anomalous behavior. The platform serves as a practical demonstration of modern security analytics and provides an excellent environment for evaluating ShaktiDB under real-world workloads.