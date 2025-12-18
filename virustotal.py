import requests
import os

API_KEY = os.getenv("VT_API_KEY")

def vt_ip_report(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": API_KEY}
    r = requests.get(url, headers=headers)
    return r.json()
