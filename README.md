# SentinelAI 🔐

SentinelAI is a modular, AI-enhanced cybersecurity platform built with Flask. It provides real-time anomaly detection, risk scoring, plugin-based extensibility, GDPR/KVKK compliance tools, and more — all with a professional-grade architecture ready for deployment.

---

## 🚀 Features

- 🧠 AI-Based CVSS Scoring
- 📊 Real-Time KPI Analytics
- 🧩 Plugin Executor & Loader System
- 📍 GeoIP IP Mapping
- 🔐 OAuth Login (Google)
- 🔑 JWT + Role-Based Access
- 🗄️ Log Archiving System
- 🧪 Dummy Log Generator (Training)
- 🌐 Swagger UI API Documentation
- 📦 Docker-Ready Deployment

---

## 📁 Project Structure

```
SentinelAI_Pro/
├── app/
│   ├── api/                # Modular API endpoints (KPI, plugins, geoip)
│   ├── auth/               # Login, LDAP, OAuth, JWT guard
│   ├── ai/                 # CVSS scoring logic
│   ├── plugins/            # Executable user plugins
│   ├── visual/             # GeoIP visualization
│   ├── archive/            # Log archiving
│   ├── train/              # Dummy data generation
│   └── swagger_config.py   # Swagger documentation config
├── static/                 # PWA assets (manifest, sw.js)
├── data/logs/              # Log storage
├── Dockerfile
├── docker-compose.yml
├── install.sh
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

```bash
# Install Docker & Docker Compose
./install.sh
# or manually
docker-compose up --build -d
```

Then visit: [http://localhost:5000](http://localhost:5000)  
Swagger UI: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## 🔐 OAuth Login

SentinelAI supports Google login. Add your credentials to a `.env` file:

```env
OAUTH_GOOGLE_CLIENT_ID=xxx
OAUTH_GOOGLE_CLIENT_SECRET=xxx
SECRET_KEY=sentinel_secret
```

Then visit: `/login/google`

---

## 🛠️ Notes

- JWT-based access control is enforced
- Roles: `viewer`, `analyst`, `admin`
- Modular blueprint system with secure API design
