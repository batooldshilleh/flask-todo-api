from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import sqlite3
import asyncio

app = FastAPI()
DB_FILE = "todo.db"

# تعريف النموذج للطلب
class Item(BaseModel):
    task: str

# إنشاء الجدول لو مش موجود
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
            )
        """)

@app.on_event("startup")
def startup_event():
    init_db()

# GET /items
@app.get("/items")
async def get_items():
    await asyncio.sleep(0)  # لتحاكي I/O غير متزامن
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT id, task FROM items")
        items = [{"id": row[0], "task": row[1]} for row in cursor.fetchall()]
    return items

# POST /items
@app.post("/items", status_code=201)
async def add_item(item: Item):
    await asyncio.sleep(0)
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("INSERT INTO items (task) VALUES (?)", (item.task,))
        item_id = cursor.lastrowid
    return {"id": item_id, "task": item.task}
