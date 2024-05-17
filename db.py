import sqlite3

from models.task import Task


def create_database():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)"""
    )
    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return [Task(id=row[0], task=row[1]) for row in tasks]


def add_task(task: str):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    id = c.lastrowid
    conn.commit()
    conn.close()
    return Task(id=id, task=task)


def delete_task(task_id: int):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
