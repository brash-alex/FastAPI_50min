from typing import Annotated
from fastapi import Depends, APIRouter
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()],) -> STaskId:
    tasks_id = await TaskRepository.add_one(task)
    return {"OK": True, "task_id": tasks_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks




