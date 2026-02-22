from src.core.task import Task
from src.core.workflow import Workflow
from src.core.executor import WorkflowExecutor


def task_a():
    print("Running A")
    return 1


def task_b(a: int):
    print("Running B")
    return a + 2


def task_c(a: int):
    print("Running C")
    return a * 3


def task_d(b: int, c: int):
    print("Running D")
    return b + c


if __name__ == "__main__":
    wf = Workflow("demo")

    t_a = Task("a", task_a)
    t_b = Task("b", lambda a: task_b(a))
    t_c = Task("c", lambda a: task_c(a))
    t_d = Task("d", lambda b, c: task_d(b, c))

    wf.add_task(t_a)
    wf.add_task(t_b, depends_on=["a"])
    wf.add_task(t_c, depends_on=["a"])
    wf.add_task(t_d, depends_on=["b", "c"])

    executor = WorkflowExecutor(wf)
    final_context = executor.run()
    print("Final context:", final_context)
