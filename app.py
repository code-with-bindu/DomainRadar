from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import httpx
import socket
import dns.resolver
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_home():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

@app.get("/lookup")
async def lookup(domain: str):
    result = {}

    # Clean input
    domain = domain.strip().replace("https://", "").replace("http://", "").replace("www.", "").split("/")[0]
    result["domain"] = domain

    # 1. Resolve IP address
    try:
        ip = socket.gethostbyname(domain)
        result["ip"] = ip
    except Exception:
        result["ip"] = "Could not resolve"
        return result

    # 2. Geo + ISP info from ip-api
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            geo = await client.get(f"http://ip-api.com/json/{ip}")
            geo_data = geo.json()
            result["country"]     = geo_data.get("country", "Unknown")
            result["country_code"]= geo_data.get("countryCode", "")
            result["region"]      = geo_data.get("regionName", "Unknown")
            result["city"]        = geo_data.get("city", "Unknown")
            result["isp"]         = geo_data.get("isp", "Unknown")
            result["org"]         = geo_data.get("org", "Unknown")
            result["timezone"]    = geo_data.get("timezone", "Unknown")
            result["lat"]         = geo_data.get("lat", 0)
            result["lon"]         = geo_data.get("lon", 0)
    except Exception:
        result["country"] = "Unknown"

    # 3. DNS Records
    dns_records = {}

    # A record
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        dns_records["A"] = [str(r) for r in a_records]
    except Exception:
        dns_records["A"] = []

    # MX record
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        dns_records["MX"] = [str(r.exchange) for r in mx_records]
    except Exception:
        dns_records["MX"] = []

    # NS record
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        dns_records["NS"] = [str(r) for r in ns_records]
    except Exception:
        dns_records["NS"] = []

    # TXT record
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        dns_records["TXT"] = [str(r) for r in txt_records][:2]
    except Exception:
        dns_records["TXT"] = []

    # CNAME record
    try:
        cname = dns.resolver.resolve(domain, 'CNAME')
        dns_records["CNAME"] = [str(r) for r in cname]
    except Exception:
        dns_records["CNAME"] = []

    result["dns"] = dns_records

    # 4. Reverse DNS
    try:
        reverse = socket.gethostbyaddr(ip)
        result["reverse_dns"] = reverse[0]
    except Exception:
        result["reverse_dns"] = "Not available"

    return result