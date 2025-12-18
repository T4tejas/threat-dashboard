from OTXv2 import OTXv2
import os

otx = OTXv2(os.getenv("OTX_API_KEY"))

def get_ip_reputation(ip):
    return otx.get_indicator_details_by_section(
        "IPv4", ip, "general"
    )
