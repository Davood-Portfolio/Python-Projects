from typing import Dict, Any, Set
from .workflow import Workflow


class WorkflowExecutor:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow

    def run(self, context: Dict[str, Any] | None = None):
        context = context or {}
        completed: Set[str] = set()

        while len(completed) < len(self.workflow.tasks):
            ready_tasks = self.workflow._ready_tasks(completed)
            if not ready_tasks:
                raise RuntimeError(
                    "No runnable tasks but workflow not completed. Possible circular dependency."
                )

            for task in ready_tasks:
                result = task.run(**context)
                context[task.name] = result
                completed.add(task.name)

        return context
