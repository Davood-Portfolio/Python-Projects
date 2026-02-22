from src.core.task import Task, TaskStatus


def test_task_success():
    def add():
        return 10

    task = Task("add", add)
    result = task.run()

    assert result == 10
    assert task.status == TaskStatus.SUCCESS
    assert task.error is None


def test_task_failure():
    def fail():
        raise ValueError("boom")

    task = Task("fail", fail)

    try:
        task.run()
    except ValueError:
        pass

    assert task.status == TaskStatus.FAILED
    assert isinstance(task.error, Exception)
