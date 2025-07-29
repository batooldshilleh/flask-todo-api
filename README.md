
# 📝 Todo API Project

This is a simple Todo API built in Python. It was developed in 3 progressive stages:

1. **Flask + In-Memory**: basic API with `GET` and `POST` endpoints
2. **Flask + SQLite**: added persistence using a lightweight database
3. **FastAPI + Async + SQLite**: optimized version with asynchronous request handling

---

## 🚀 Features

- `GET /items`: Returns all todo tasks
- `POST /items`: Adds a new todo task
- Uses SQLite for storage
- FastAPI version supports async
- Includes performance testing script
- Ready for Docker or production upgrades

---

## 🧪 Testing Tools Used

- `curl` – API interaction
- `curl -w` – Response time measurement
- `time` – Command execution time
- `htop` – CPU & memory usage monitoring
- `Chrome DevTools` – Network inspection
- `multiprocessing` script – Simulated load test

---

## 📂 Project Structure

```

flask-todo-api/
├── app.py              # Flask version (sync, with SQLite)
├── main.py             # FastAPI version (async, with SQLite)
├── load\_test.py        # Python script to simulate stress testing
├── curl-format.txt     # Custom format for measuring curl timings
├── Report.pdf          # Final analysis report
└── README.md           # You're reading it now :)

````

---

## 💡 Improvements & Future Work

- Use PostgreSQL instead of SQLite for concurrent writes
- Add async database access via SQLModel
- Add Redis for caching and performance
- Implement unit testing with pytest
- Add rate limiting, authentication, and Docker support

---

## 📦 How to Run

### Flask:

```bash
python app.py
````

### FastAPI:

```bash
uvicorn main:app --reload --port 8000
```

---

