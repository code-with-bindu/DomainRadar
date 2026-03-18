# 🌐 DomainRadar — IP & DNS Lookup Tool

> Instantly reveal the IP address, geolocation, ISP, and full DNS records of any domain.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=flat-square)
![dnspython](https://img.shields.io/badge/dnspython-DNS%20Records-purple?style=flat-square)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Deployed-yellow?style=flat-square)

---

## 🔴 Live Demo
👉 [Try it on Hugging Face](https://huggingface.co/spaces/HumanSpace/domainradar)

---

## 📌 What It Does

DomainRadar is a real-time network intelligence tool. Enter any domain name and instantly get:

| Feature | Description |
|---|---|
| 🌍 IP Address | Resolves the domain to its real IP |
| 📍 Geolocation | Country, city, region, coordinates |
| 🏢 ISP & Org | Internet Service Provider and organization |
| 🕐 Timezone | Server timezone information |
| 📡 DNS Records | A, MX, NS, TXT, CNAME records |
| 🔄 Reverse DNS | Reverse lookup of the IP address |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| DNS Resolution | dnspython |
| IP Geolocation | ip-api.com (free live API) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Hugging Face Spaces (Docker) |

---

## 📁 Project Structure

```
domainradar/
├── app.py              # FastAPI backend + DNS + IP lookup logic
├── index.html          # Frontend UI
├── requirements.txt    # Python dependencies
└── Dockerfile          # For Hugging Face deployment
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/domainradar.git
cd domainradar

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
uvicorn app:app --reload

# 4. Open in browser
http://localhost:8000
```

---

## 📊 Sample Output

For `github.com`:

| Field | Value |
|---|---|
| IP Address | 140.82.121.4 |
| Country | United States |
| City | Seattle |
| ISP | Microsoft Corporation |
| A Record | 140.82.121.4 |
| NS Record | ns-1283.awsdns-32.org |
| MX Record | aspmx.l.google.com |

---

## 🌐 Try These Domains

- `google.com` → Google servers, USA
- `flipkart.com` → India based servers
- `github.com` → Microsoft/GitHub ISP
- `openai.com` → Cloudflare ISP


---

> ⚠️ This tool is for educational and informational purposes only. Do not use for malicious intent.