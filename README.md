# ShaktiSOC

### AI-Powered Security Operations Center using ShaktiDB

A full-stack cybersecurity monitoring platform that collects real-time Linux system telemetry, stores security events in ShaktiDB (PostgreSQL), analyzes threats using a context-aware machine learning engine, and visualizes high-fidelity alerts on a live React dashboard.

---

## Project Overview

ShaktiSOC continuously monitors a Linux endpoint across multiple attack vectors - CPU/process activity, SSH authentication, network sockets, and file system integrity. Collected telemetry is ingested into ShaktiDB and analyzed by an Isolation Forest ML model enhanced with process whitelisting, hard thresholds, and multi-vector correlation to eliminate alert fatigue and surface only actionable threats.

### Key Capabilities

* **Multi-Vector Telemetry** - Collects process, login, network, and file system events in real time
* **Context-Aware AI Engine** - Isolation Forest with whitelisting, hard thresholds (>10% CPU/Memory), and 1% contamination rate
* **Cross-Vector Correlation** - Detects coordinated attacks by correlating CPU spikes with simultaneous file modifications and network activity
* **Live Dashboard** - React + Tailwind UI with 5-second polling, interactive charts, and color-coded severity indicators
* **Automated Data Retention** - Prunes telemetry older than 7 days to keep the database lean

---

## Architecture

```text
Linux Endpoint (Ubuntu 22.04)
│
├── Process Events ─────── process_collector.py (psutil)
├── SSH Login Events ───── login_collector.py (auth.log tail)
├── Network Sockets ────── network_collector.py (psutil)
└── File System Events ─── file_collector.py (watchdog)
        │
        ▼
  ShaktiDB (PostgreSQL)
  ┌─────────────────────────────────────────┐
  │ ProcessLogs │ LoginLogs │ NetworkLogs   │
  │ FileLogs    │ Alerts    │ Users         │
  └─────────────────────────────────────────┘
        │
        ▼
  AI Threat Engine (Isolation Forest + Correlation)
        │
        ▼
  Flask REST API (Port 5000)
        │
        ▼
  React Dashboard (Vite + Tailwind CSS)
```

---

## Repository Structure

```
shaktidb-work/
├── README.md                           # This file
├── shaktisoc/                          # Main application source code
│   ├── collectors/                     # Telemetry collection daemons
│   │   ├── process_collector.py        # CPU/Memory process monitoring
│   │   ├── login_collector.py          # SSH auth.log parser
│   │   ├── network_collector.py        # TCP/UDP socket scanner
│   │   └── file_collector.py           # File integrity monitor (watchdog)
│   ├── analytics/                      # AI threat detection
│   │   └── threat_detector.py          # Isolation Forest + Correlation Engine
│   ├── dashboard/                      # Backend API
│   │   └── api.py                      # Flask REST API server
│   ├── db/                             # Database layer
│   │   ├── schema.sql                  # Table definitions
│   │   └── connection.py               # PostgreSQL connection manager
│   ├── shaktisoc-ui/                   # Frontend dashboard
│   │   ├── src/App.jsx                 # Main React dashboard component
│   │   ├── package.json                # Node.js dependencies
│   │   └── ...                         # Vite + Tailwind configuration
│   └── requirements.txt               # Python dependencies
├── docs/                               # Project documentation
│   ├── architecture.md                 # System architecture document
│   ├── project-proposal.md             # Original project proposal
│   └── system-info.md                  # System information
├── reports/                            # Weekly progress reports
│   ├── week1-report.md                 # Weeks 1 through 7
│   └── ...
├── installation/                       # ShaktiDB installation files & notes
│   ├── installation-notes.md           # Step-by-step installation guide
│   └── shaktidb_17.7.1.1_amd64.deb    # ShaktiDB installer package
├── scripts/                            # Shell scripting utilities
│   └── dev_setup_tool.sh              # Interactive system info tool
└── bugs/                               # Documented ShaktiDB issues
```

---

## Technology Stack

| Layer            | Technology                                           |
| ---------------- | ---------------------------------------------------- |
| **Database**     | ShaktiDB (PostgreSQL-compatible)                     |
| **Backend**      | Python 3, Flask 3.0, Flask-CORS                      |
| **AI/ML**        | Scikit-Learn (Isolation Forest), Pandas, NumPy       |
| **Telemetry**    | psutil, watchdog, subprocess (auth.log)              |
| **Frontend**     | React 19, Vite 8, Tailwind CSS 3                     |
| **Charting**     | Recharts, Lucide React (icons)                       |
| **Data Fetch**   | Axios (async polling at 5-second intervals)          |
| **OS**           | Ubuntu 22.04 LTS                                     |
| **Version Control** | Git, GitHub                                       |

---

## Database Schema

| Table          | Purpose                                        |
| -------------- | ---------------------------------------------- |
| `Users`        | User accounts and roles                        |
| `ProcessLogs`  | High-CPU/Memory process snapshots              |
| `LoginLogs`    | SSH authentication events (success/failure)    |
| `NetworkLogs`  | Active TCP/UDP socket connections              |
| `FileLogs`     | File create/modify/delete events               |
| `Alerts`       | AI-generated security alerts with severity     |

---

## Getting Started

### Prerequisites

* Ubuntu 22.04 LTS
* ShaktiDB (PostgreSQL) installed and running
* Python 3.10+
* Node.js 18+

### 1. Database Setup

```bash
# Create the database
psql -U postgres -c "CREATE DATABASE shaktisoc;"

# Apply the schema
psql -U postgres -d shaktisoc -f shaktisoc/db/schema.sql
```

### 2. Configure Environment Variables

```bash
export SHAKTI_DB_NAME="shaktisoc"
export SHAKTI_DB_USER="postgres"
export SHAKTI_DB_PASSWORD="your_password"
export SHAKTI_DB_HOST="127.0.0.1"
export SHAKTI_DB_PORT="5432"
```

### 3. Install Python Dependencies

```bash
cd shaktisoc
pip install -r requirements.txt
```

### Step 1: Start the Sensors (The Collectors)

Open four separate terminal windows, navigate to your `shaktisoc` folder in each, and start your data collectors:

* **Terminal 1:** `python3 collectors/process_collector.py`
* **Terminal 2:** `python3 collectors/network_collector.py`
* **Terminal 3:** `python3 collectors/file_collector.py`
* **Terminal 4:** `sudo python3 collectors/login_collector.py`

### Step 2: Start the Brain & The API (The Backend)

Open two more terminal windows to start the analysis and routing layers:

* **Terminal 5:** `python3 analytics/threat_detector.py`
* **Terminal 6:** `python3 dashboard/api.py`

### Step 3: Start the Glass (The Frontend)

Open one last terminal, navigate into your UI folder, and start the React app:

* **Terminal 7:**
  ```bash
  cd shaktisoc-ui
  npm run dev
  ```

Open the provided local URL (usually `http://localhost:5173`) in your web browser. You should see your dashboard showing "System Secure" with empty tables (since we just wiped the database).

---

## Execute the Multi-Vector Attack

Now for the fun part. We are going to simulate a hacker breaching your system, dropping a payload, calling out to a command-and-control server, and executing a cryptominer.

Open an **Eighth Terminal** and run these two commands:

**1. The SSH Brute Force Simulation:**
```bash
ssh fakeuser@localhost
```
*(Type any random password and hit enter to fail the login).*

**2. The Payload Execution:** (Run this exactly as written)
```bash
touch /tmp/malware.sh && curl -s http://google.com > /dev/null && echo "scale=5000; a(1)*4" | bc -l
```

### Watch the Dashboard

Switch immediately back to your web browser and watch the dashboard over the next 30 seconds. You will see:

* **Authentication Logs (Bottom Left):** A red `FAILED` login attempt will appear for `fakeuser`.
* **File Integrity Monitor (Bottom Right):** You will see `/tmp/malware.sh` flagged as `CREATED`.
* **Network Sockets (Bottom Middle):** You will see a new `ESTABLISHED` TCP connection mapping to an external IP address (triggered by the curl command).
* **Live Resource Telemetry (Center Graph):** The `bc` process will suddenly appear on the graph with a massive CPU spike.
* **AI Threat Engine Alerts (Top Left):** The Threat Engine will detect the CPU spike, cross-reference the exact timestamp with the File and Network logs, and generate a **CRITICAL • MALWARE_BEHAVIOR** super-alert warning you of a correlated attack!

---

## API Endpoints

| Method | Endpoint               | Description                         |
| ------ | ---------------------- | ----------------------------------- |
| GET    | `/api/status`          | API health check                    |
| GET    | `/api/logs/processes`  | Latest 50 process telemetry events  |
| GET    | `/api/logs/logins`     | Latest 50 SSH authentication events |
| GET    | `/api/logs/network`    | Latest 50 network socket events     |
| GET    | `/api/logs/files`      | Latest 50 file system events        |
| GET    | `/api/logs/alerts`     | Latest 50 AI-generated alerts       |

All endpoints return JSON. The API runs on `http://127.0.0.1:5000`.

---

## AI Threat Detection

The threat engine uses a tuned **Isolation Forest** model to detect anomalous process behavior:

1. **Process Whitelisting** - Known safe processes (Chrome, Firefox, VS Code, systemd, etc.) are excluded from ML analysis to eliminate false positives
2. **Hard Thresholds** - Anomalies must also exceed 10% CPU or 10% Memory to qualify as threats
3. **Low Contamination** - Set at 1% to ensure only statistically significant outliers trigger alerts
4. **Multi-Vector Correlation** - If a CPU anomaly coincides with file modifications and new network connections, the alert is escalated to `CRITICAL` severity as a potential coordinated attack
5. **Automated Pruning** - Telemetry older than 7 days is automatically purged every hour of runtime

---

## Dashboard Features

* **System Status Indicator** - Live connection status with animated pulse
* **AI Threat Engine Alerts** - Color-coded severity panel (HIGH / CRITICAL)
* **Live CPU Telemetry Chart** - Real-time line chart powered by Recharts
* **Authentication Logs** - SSH login events with success/failure indicators
* **Network Socket States** - Active connections with protocol and status
* **File Integrity Monitor** - File system events with action type highlighting

---

## Project Status

| Module                     | Status                     |
| -------------------------- | -------------------------- |
| Database Integration       | ✅ Completed               |
| Core Telemetry Collectors  | ✅ Completed               |
| Advanced Telemetry (Net/FIM) | ✅ Completed             |
| Backend REST API           | ✅ Completed               |
| AI Threat Engine           | ✅ Completed (Production Tuned) |
| Web Dashboard              | ✅ Completed (Tailwind UI) |
| **Project**                | **✅ Successfully Delivered** |

---

## Future Scope

* Advanced deep learning models for threat detection
* Automated incident response and remediation
* Multi-host distributed monitoring
* Threat intelligence feed integration
* AI-assisted forensic analysis

---

## Weekly Reports

| Week | Duration                    | Focus Area                                    |
| ---- | --------------------------- | --------------------------------------------- |
| 1    | 19 May – 25 May 2026       | Environment setup, ShaktiDB installation      |
| 2    | 26 May – 01 Jun 2026       | Project proposal, architecture design         |
| 3    | 02 Jun – 08 Jun 2026       | Database schema, core collectors               |
| 4    | 09 Jun – 15 Jun 2026       | Network & file collectors, initial API         |
| 5    | 16 Jun – 22 Jun 2026       | AI threat engine, Isolation Forest             |
| 6    | 23 Jun – 29 Jun 2026       | Correlation engine, alert fatigue mitigation   |
| 7    | 30 Jun – 06 Jul 2026       | React dashboard, end-to-end integration        |

---

## Author

**Rasal Musthafa**

B.Tech Computer Science & Engineering

ShaktiSOC Project - ShaktiDB Workspace
