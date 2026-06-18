-- Table to store information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    usrname VARCHAR(50) UNIQUE NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    cretaed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store login attempts
CREATE TABLE LoginLogs (
    log_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    status VARCHAR(20),
    source_ip VARCHAR(45),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Table to store running processes
CREATE TABLE ProcessLogs (
    process_id SERIAL PRIMARY KEY,
    pid INT,
    process_name VARCHAR(100),
    cpu_usage FLOAT,
    memory_usage FLOAT,
    username VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store Security alerts
CREATE TABLE Alerts (
    alert_id SERIAL PRIMARY KEY,
    event_type VARCHAR(50),
    description TEXT,
    severity VARCHAR(10),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store Network connections (TCP/UDP)
CREATE TABLE NetworkLogs (
    log_id SERIAL PRIMARY KEY,
    local_ip VARCHAR(45),
    local_port INT,
    remote_ip VARCHAR(45),
    remote_port INT,
    protocol VARCHAR(10),
    status VARCHAR(20),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store File System events
CREATE TABLE FileLogs (
    log_id SERIAL PRIMARY KEY,
    file_path TEXT,
    action_type VARCHAR(50), -- e.g., 'CREATED', 'MODIFIED', 'DELETED'
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);