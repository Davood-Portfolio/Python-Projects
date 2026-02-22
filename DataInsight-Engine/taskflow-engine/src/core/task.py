from enum import Enum
from typing import Callable, Any, Dict, Optional


class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Task:
    def __init__(self, name: str, func: Callable[..., Any]):
        self.name = name
        self.func = func
        self.status = TaskStatus.PENDING
        self.result: Optional[Any] = None
        self.error: Optional[Exception] = None

    def run(self, **kwargs) -> Any:
        self.status = TaskStatus.RUNNING
        try:
            self.result = self.func(**kwargs)
            self.status = TaskStatus.SUCCESS
            return self.result
        except Exception as e:
            self.status = TaskStatus.FAILED
            self.error = e
            raise
