# """
# Part 6: Homework - Personal To-Do List App
# ==========================================
# See Instruction.md for full requirements.

# How to Run:
# 1. Make sure venv is activated
# 2. Run: python app.py
# 3. Open browser: http://localhost:5000
# """

# from flask import Flask, render_template

# app = Flask(__name__)

# # Sample data - your tasks list
# TASKS = [
#     {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
#     {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
#     {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
# ]

# # Your code here...

# @app.route('/')
# def home():
#     return render_template('index.html', tasks=TASKS)


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ---------- DATABASE FUNCTION ----------
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

# ---------- CREATE TABLE (RUN ONCE) ----------
conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    priority TEXT NOT NULL
)
""")
conn.commit()
conn.close()

# ---------- HOME ----------
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# ---------- ADD TASK ----------
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    priority = request.form['priority']

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO tasks (title, status, priority) VALUES (?, ?, ?)',
        (title, 'Pending', priority)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# ---------- COMPLETE TASK ----------
@app.route('/complete/<int:id>')
def complete_task(id):
    conn = get_db_connection()
    conn.execute(
        'UPDATE tasks SET status = ? WHERE id = ?',
        ('Completed', id)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# ---------- DELETE TASK ----------
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
