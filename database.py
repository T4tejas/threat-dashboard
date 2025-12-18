CREATE TABLE threat_intel (
    id SERIAL PRIMARY KEY,
    source TEXT,
    ip INET,
    threat_score INT,
    country TEXT,
    malicious BOOLEAN,
    timestamp TIMESTAMP
);
