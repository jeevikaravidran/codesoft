todo_list=[]

def menu():
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Mark task as done")
        print("6. Exit")


def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "Status": "Pending"})
    print("New task added successfully.\n")


def view_tasks():
    print("To-Do List:")
    if len(todo_list) == 0:
        print("No tasks available.\n")
    else:
        for index, item in enumerate(todo_list,1):
            print(f"{index}. {item['task']} - {item['Status']}")
    print("\n") 


def remove_task():
        if len(todo_list) == 0:
            print("No tasks to remove.\n")
        else:
            try:
                search_index = int(input("Enter the task number to remove: ")) - 1
                if 0<=search_index < len(todo_list):
                    removed_task = todo_list.pop(search_index)
                    print(f"Task Removed: {removed_task['task']}\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")

def edit_task():
        if len(todo_list) == 0:
            print("No tasks to edit.\n")
        else:
            try:
                search_index = int(input("Enter the task number to edit: ")) - 1
                if 0<=search_index < len(todo_list):
                    new_task = input("Enter the new task description: ")
                    todo_list[search_index]['task'] = new_task
                    print("Task updated successfully.\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")


def mark_done():
        if len(todo_list) == 0:
            print("No tasks to mark as done.\n")
        else:
            try:
                search_index = int(input("Enter the task number to mark as Completed: ")) - 1
                if 0<=search_index < len(todo_list):
                    todo_list[search_index]['Status'] = "Completed"
                    print(f"Task {todo_list[search_index]['task']} has been marked as Completed.\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")

while (True):
    menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        edit_task()
    elif choice == '5':
        mark_done()
    elif choice == '6':
        print("Exiting the application!!!.")
        exit()
    else:
        print("Invalid choice!.Please try again.")