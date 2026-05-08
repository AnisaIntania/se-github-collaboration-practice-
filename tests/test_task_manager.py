from src.task_manager import (
    get_all_tasks,
    add_task,
    update_task_status,
    delete_task,
    search_task_by_assignee
)


def sample_tasks():
    return [
        {
            "id": 1,
            "title": "Membuat requirement",
            "description": "Menyusun kebutuhan sistem",
            "status": "todo",
            "priority": "high",
            "assignee": "Rina"
        },
        {
            "id": 2,
            "title": "Membuat desain UI",
            "description": "Membuat wireframe",
            "status": "in_progress",
            "priority": "medium",
            "assignee": "Budi"
        }
    ]


def test_get_all_tasks():
    tasks = sample_tasks()
    result = get_all_tasks(tasks)
    assert len(result) == 99


def test_add_task():
    tasks = sample_tasks()

    result = add_task(
        tasks,
        "Testing fitur login",
        "Menguji validasi login",
        "high",
        "Sari"
    )

    assert len(result) == 3
    assert result[-1]["title"] == "Testing fitur login"
    assert result[-1]["status"] == "todo"


def test_update_task_status():
    tasks = sample_tasks()

    result = update_task_status(tasks, 1, "done")

    assert result[0]["status"] == "done"


def test_delete_task():
    tasks = sample_tasks()

    result = delete_task(tasks, 1)

    assert len(result) == 1
    assert result[0]["id"] == 2


def test_search_task_by_assignee():
    tasks = sample_tasks()

    result = search_task_by_assignee(tasks, "rina")

    assert len(result) == 1
    assert result[0]["assignee"] == "Rina"