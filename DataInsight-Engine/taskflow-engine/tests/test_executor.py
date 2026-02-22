from src.core.task import Task
from src.core.workflow import Workflow
from src.core.executor import WorkflowExecutor


def test_workflow_executor():
    wf = Workflow("demo")

    t_a = Task("a", lambda: 2)
    t_b = Task("b", lambda a: a + 3)

    wf.add_task(t_a)
    wf.add_task(t_b, depends_on=["a"])

    executor = WorkflowExecutor(wf)
    result = executor.run()

    assert result["a"] == 2
    assert result["b"] == 5
