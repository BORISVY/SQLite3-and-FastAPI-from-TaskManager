from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import sys
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
def listar_tarefas():
    return manager.get_all_tasks()

@app.get("/tarefas/{task_id}")
def get_task(task_id: int):
    task = manager.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.post("/tarefas", status_code=201)
def create_task(task: TaskCreate):
    try:
        manager.create_task(task.title, task.desc)
        return {"message": "Tarefa criada!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/tarefas/{task_id}")
def delete_task(task_id: int):
    deleted = manager.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa removida com sucesso"}

@app.patch("/tarefas/{task_id}/concluir")
def complete_task(task_id: int):
    updated = manager.complete_task(task_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa concluída"}

@app.patch("/tarefas/{task_id}/reabrir")
def reopen_task(task_id: int):
    updated = manager.reopen_task(task_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa reaberta"}

@app.get("/tarefas/buscar/")
def search_tasks(title: str):
    results = manager.search_tasks(title)

    if not results:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada")

    return results