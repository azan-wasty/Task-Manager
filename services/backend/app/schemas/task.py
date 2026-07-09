import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from app.models.task import TaskStatus

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, examples=["Buy groceries"])
    description: Optional[str] = Field(None, examples=["Milk, eggs, bread"])
    status: TaskStatus = TaskStatus.PENDING

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

class TaskOut(TaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)