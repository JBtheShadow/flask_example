import db
from flask import Blueprint, redirect, render_template, request, url_for

tasks_page = Blueprint("tasks_page", __name__)


@tasks_page.get("/")
def index():
    tasks = db.get_tasks()
    return render_template("index.html", tasks=tasks)


@tasks_page.post("/add")
def add_task():
    task = request.form["task"]
    db.add_task(task)
    return redirect(url_for("tasks_page.index"))


@tasks_page.get("/delete/<int:task_id>")
def delete_task(task_id):
    db.delete_task(task_id)
    return redirect(url_for("tasks_page.index"))
