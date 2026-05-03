from task_manager import show_tasks, add_task, update_status, delete_task, search_by_assignee

def main():
    while True:
        print("\n=== To-Do List Project ===")
        print("1. Tampilkan semua task")
        print("2. Tambah task")
        print("3. Ubah status task")
        print("4. Hapus task")
        print("5. Cari task berdasarkan assignee")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_by_assignee()
        elif choice == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
