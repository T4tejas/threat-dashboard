import requests
import os

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def get_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    r = requests.get(url, headers=headers, params=params)
    return r.json()
