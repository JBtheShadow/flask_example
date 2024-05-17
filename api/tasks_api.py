from flask import Response
from flask_openapi3.blueprint import APIBlueprint

import db as db
from models.task import (
    CreateTaskRequestBody,
    CreateTaskRequestForm,
    DeleteTaskRequestPath,
    GetTasksRequestQuery,
    Task,
)

tasks_api = APIBlueprint("tasks_api", __name__)


@tasks_api.get("/api/tasks/", responses={200: Task})
def get_tasks(query: GetTasksRequestQuery):
    tasks = sorted(db.get_tasks(), key=lambda x: x.id, reverse=not query.asc)
    return [x.model_dump() for x in tasks]


@tasks_api.post("/api/tasks/", responses={200: Task})
def create_task(body: CreateTaskRequestBody):
    return db.add_task(body.task).model_dump()


@tasks_api.post("/api/form/tasks/", responses={200: Task})
def create_task_via_form(form: CreateTaskRequestForm):
    return db.add_task(form.task).model_dump()


@tasks_api.delete("/api/tasks/<int:id>", responses={200: None})
def delete(path: DeleteTaskRequestPath):
    db.delete_task(path.id)
    return Response(status=200)
