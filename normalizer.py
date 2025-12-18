def normalize_ip_threat(source, data):
    return {
        "source": source,
        "ip": data.get("ip"),
        "threat_score": data.get("score"),
        "country": data.get("country"),
        "asn": data.get("asn"),
        "malicious": data.get("malicious"),
        "timestamp": data.get("timestamp")
    }
