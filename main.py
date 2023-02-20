from celery.result import AsyncResult
from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import JSONResponse
from worker import create_task


app = FastAPI()


@app.get("/")
def home(request: Request):
    return JSONResponse({"message": "Hello world"})


@app.post("/tasks", status_code=201)
def run_task(task_type: int = Form(default=10)):
    task = create_task.delay(int(task_type))
    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)