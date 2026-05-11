import json

DATA_FILE = "data/tasks.json"

def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks():
    tasks = load_tasks()
    print("\nDaftar Task:")
    for task in tasks:
        print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")

def add_task():
    tasks = load_tasks()
    new_id = max(task["id"] for task in tasks) + 1

    title = input("Judul task: ")
    description = input("Deskripsi: ")

    #Validasi input priority (modiefied by anisa)
    priority = input("Priority (low/medium/high): ").lower()
    #Validasi kosong
    if priority == "":
        print("Priority tidak boleh kosong!")
        return
    #Validasi input yg benar
    if priority not in ["low", "medium", "high"]:
        print("Priority tidak valid! Gunakan: low, medium, atau high.")
        return

    assignee = input("Assignee: ")

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "assignee": assignee
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task berhasil ditambahkan.")

def update_status():
    tasks = load_tasks()
    task_id = int(input("Masukkan ID task: "))
    new_status = input("Status baru (todo/in_progress/done): ")

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print("Status berhasil diubah.")
            return

    print("Task tidak ditemukan.")

def delete_task():
    tasks = load_tasks()
    task_id = int(input("Masukkan ID task: "))

    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task tidak ditemukan.")
    else:
        save_tasks(new_tasks)
        print("Task berhasil dihapus.")

def search_by_assignee():
    tasks = load_tasks()
    keyword = input("Masukkan nama assignee: ").lower()

    results = [task for task in tasks if keyword in task["assignee"].lower()]

    if not results:
        print("Task tidak ditemukan.")
    else:
        print("\nHasil pencarian:")
        for task in results:
            print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")
