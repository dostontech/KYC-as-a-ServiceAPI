# KYC-as-a-ServiceAPI

A simple KYC + AML demo service built with FastAPI, PostgreSQL and Docker. This project is for learning and demonstration only.

## Quick start

Requirements:
- Docker Desktop (Windows/Mac) with Compose
- Python 3.13 (for local dev if you want to run without Docker)

1. Clone the repo

```bash
git clone (https://github.com/dostontech/KYC-as-a-ServiceAPI)
cd kyc-as-a-serviceapi
```

2. Start services via Docker

```bash
docker-compose up --build -d
```

3. Start the backend (optional if running in container already)

```bash
# if running locally
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

4. Open docs

Visit http://localhost:8000/docs

## API Endpoints
- `POST /users/` — create user
- `GET  /users/` — list users
- `POST /kyc/submit` — submit KYC request
- `GET  /kyc/status/{kyc_id}` — get KYC status
- `POST /aml/check` — run AML check (random PASS/FAIL for demo)

## Notes
- Audit logs are written to `audit_logs` table
- This is not production ready. Do not store PII in plain-text in production.
