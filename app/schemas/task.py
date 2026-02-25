from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    is_completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    is_completed: bool | None = None


class TaskResponse(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
