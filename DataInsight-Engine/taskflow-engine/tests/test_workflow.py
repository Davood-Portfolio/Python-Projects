from src.core.workflow import Workflow
from src.core.task import Task


def test_workflow_dependencies():
    wf = Workflow("test")

    t1 = Task("a", lambda: 1)
    t2 = Task("b", lambda a: a + 1)

    wf.add_task(t1)
    wf.add_task(t2, depends_on=["a"])

    ready = wf._ready_tasks(set())
    assert len(ready) == 1
    assert ready[0].name == "a"

    ready_after_a = wf._ready_tasks({"a"})
    assert len(ready_after_a) == 1
    assert ready_after_a[0].name == "b"
