# KYC-as-a-Service API

A simple **KYC (Know Your Customer) + AML (Anti-Money Laundering)** demo service built with **FastAPI**, **PostgreSQL**, and **Docker**.
This project is for **learning and demonstration purposes only** — **not** for production use.

---

## Purpose

This project demonstrates how to implement a **KYC verification** and **AML screening API** backend service.
It covers:

* ✅ User onboarding and KYC submission
* ✅ AML checks (random PASS/FAIL for demo)
* ✅ Audit logging for compliance
* ✅ Running inside Docker for easy setup

> In real-world scenarios, KYC and AML services help banks, fintechs, and other regulated businesses meet compliance requirements.

---

## Example Use Cases

Although this is a simplified demo, similar systems are used in:

* **Digital banks** — onboarding new customers while meeting regulatory requirements
* **Crypto exchanges** — verifying user identity before enabling trading or withdrawals
* **Fintech apps** — enabling payments, lending, or investing services
* **Regulated marketplaces** — ensuring sellers and buyers are verified before transactions
* **High-value transactions** — running AML checks for large payments or transfers

---

## Quick Start

### Requirements

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac) with Compose enabled
* Python **3.13** (only if running locally without Docker)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/dostontech/KYC-as-a-ServiceAPI.git
cd KYC-as-a-ServiceAPI
```

### 2️⃣ Start services via Docker

```bash
docker-compose up --build -d
```

### 3️⃣ Run backend locally (optional)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4️⃣ Open API Docs

Once the backend is running, visit:

```bash
http://localhost:8000/docs
```

You’ll see **Swagger UI** where you can test the endpoints interactively.

---

## API Endpoints

| Method | Endpoint               | Description                               |
| ------ | ---------------------- | ----------------------------------------- |
| POST   | `/users/`              | Create a new user                         |
| GET    | `/users/`              | List all users                            |
| POST   | `/kyc/submit`          | Submit KYC request                        |
| GET    | `/kyc/status/{kyc_id}` | Get KYC request status                    |
| POST   | `/aml/check`           | Run AML check (random PASS/FAIL for demo) |

---

## Data & Audit Logs

* All actions are stored in **PostgreSQL**
* **KYC** and **AML** events are recorded in the `audit_logs` table
* In production, data must be encrypted and stored securely

---

## Notes

* ❌ Not production ready — purely educational
* ❌ Do NOT store Personally Identifiable Information (PII) in plain-text
* ✅ Code is modular and ready to be extended for real integrations (e.g., SumSub, Onfido, ComplyAdvantage)
