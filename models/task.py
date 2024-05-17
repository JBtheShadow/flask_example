from pydantic import BaseModel


class Task(BaseModel):
    id: int
    task: str


class GetTasksRequestQuery(BaseModel):
    asc: bool = True


class CreateTaskRequestForm(BaseModel):
    task: str


class CreateTaskRequestBody(BaseModel):
    task: str


class DeleteTaskRequestPath(BaseModel):
    id: int
