from typing import Dict, List, Set, Callable
from .task import Task


class Workflow:
    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}
        self.dependencies: Dict[str, List[str]] = {}  # task -> list of parents

    def add_task(self, task: Task, depends_on: List[str] | None = None):
        self.tasks[task.name] = task
        self.dependencies[task.name] = depends_on or []

    def _ready_tasks(self, completed: Set[str]) -> List[Task]:
        ready = []
        for name, deps in self.dependencies.items():
            if name in completed:
                continue
            if all(d in completed for d in deps):
                ready.append(self.tasks[name])
        return ready
