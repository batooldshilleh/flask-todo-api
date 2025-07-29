# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# اسم ملف قاعدة البيانات
DB_FILE = "todo.db"

# إنشاء الجدول إذا ما كان موجود
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
            )
        """)

# جلب كل المهام من قاعدة البيانات
@app.route('/items', methods=['GET'])
def get_items():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT id, task FROM items")
        items = [{"id": row[0], "task": row[1]} for row in cursor.fetchall()]
    return jsonify(items), 200

# إضافة مهمة جديدة إلى قاعدة البيانات
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({'error': 'Missing task field'}), 400

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("INSERT INTO items (task) VALUES (?)", (data['task'],))
        item_id = cursor.lastrowid

    new_item = {"id": item_id, "task": data['task']}
    return jsonify(new_item), 201

if __name__ == '__main__':
    init_db()  # ننشئ قاعدة البيانات أولاً
    app.run(debug=True, port=8000)
