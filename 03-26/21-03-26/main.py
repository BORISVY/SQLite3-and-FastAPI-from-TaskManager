from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append('/mnt/1962bfc0-f9ca-4c35-a3e2-7f1d23b699bd/PROGRAMAS/Cursos/Python/Estudos/03-26/14-03-26')
from manager import TaskManager

class TaskCreate(BaseModel):
    title: str
    desc: Optional[str] = ""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = TaskManager()

@app.get("/")
def home():
    return {"status": "API Online", "sistema": "Gerenciador de Tarefas"}

@app.get("/tarefas")
def listar_tarefas_api():
    manager.task_list = manager.load_task()
    return manager.task_list

@app.get("/tarefas/{task_id}")
def get_task_by_id(task_id: str):
    tasks = manager.load_task()
    task = next((t for t in tasks if t["ID"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.post("/tarefas", status_code=201)
def create_task(task: TaskCreate):
    try:
        manager.new_task(task.title, task.desc)
        return {"message": "Tarefa criada!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))