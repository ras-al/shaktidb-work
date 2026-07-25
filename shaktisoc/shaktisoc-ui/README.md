# ShaktiSOC Dashboard

Real-time security monitoring dashboard for ShaktiSOC - the AI-powered Security Operations Center.

Built with **React 19**, **Vite 8**, and **Tailwind CSS 3**.

---

## Features

* **Live System Status** - Animated connection indicator with real-time API health checks
* **AI Threat Alerts Panel** - Color-coded severity alerts from the Isolation Forest engine (HIGH / CRITICAL)
* **CPU Telemetry Chart** - Interactive line chart for process resource usage (Recharts)
* **Authentication Logs** - SSH login events with success/failure status indicators
* **Network Socket Monitor** - Active TCP/UDP connections with protocol and state
* **File Integrity Monitor** - Real-time file create/modify/delete event feed
* **Auto-Refresh** - All panels poll the backend API every 5 seconds via Axios

---

## Tech Stack

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| React 19      | UI framework                     |
| Vite 8        | Build tool & dev server          |
| Tailwind CSS 3| Utility-first styling            |
| Recharts      | Data visualization (line charts) |
| Axios         | HTTP client for API polling      |
| Lucide React  | Icon library                     |

---

## Getting Started

### Prerequisites

* Node.js 18+
* ShaktiSOC Flask API running on `http://127.0.0.1:5000`

### Install & Run

```bash
npm install
npm run dev
```

The dashboard will be available at `http://localhost:5173`.

### Build for Production

```bash
npm run build
npm run preview
```

---

## API Connection

The dashboard connects to the ShaktiSOC Flask API at `http://127.0.0.1:5000/api`. Ensure the backend is running before starting the dashboard. The following endpoints are consumed:

| Endpoint               | Dashboard Panel           |
| ---------------------- | ------------------------- |
| `/api/status`          | System status indicator   |
| `/api/logs/processes`  | CPU telemetry chart       |
| `/api/logs/logins`     | Authentication logs table |
| `/api/logs/network`    | Network socket states     |
| `/api/logs/files`      | File integrity monitor    |
| `/api/logs/alerts`     | AI threat alerts panel    |

---

## Project Structure

```
shaktisoc-ui/
├── src/
│   ├── App.jsx          # Main dashboard component
│   ├── App.css          # Component styles
│   ├── main.jsx         # React entry point
│   ├── index.css        # Tailwind base styles
│   └── assets/          # Static assets
├── public/              # Public static files
├── index.html           # HTML entry point
├── package.json         # Dependencies & scripts
├── vite.config.js       # Vite configuration
├── tailwind.config.js   # Tailwind CSS configuration
├── postcss.config.js    # PostCSS configuration
└── eslint.config.js     # ESLint configuration
```
