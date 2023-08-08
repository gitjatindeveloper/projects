def add_tasks(tasks):
    # add task - function to enter task and append it to the list as a dictionary
    task_description = input("Enter task description: ")

    # Create a dictionary to represent the task with its description and completion status
    task = {
        "description": task_description,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully")

def view_tasks(tasks):
    # view task - function to display the list of tasks
    print("** Your Task List **")
    for index, task in enumerate(tasks, 1):
        # Access individual task details using the dictionary keys
        description = task["description"]
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. task: {description}, status: {status}")

def marked_tasks(tasks, completed_tasks):
    # marked task - function to enter the task number and update its status
    view_tasks(tasks)
    task_number = int(input("Enter task number you want to mark as completed: "))

    # check task number to update task as marked or not
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        if not task["completed"]:
            task["completed"] = True
            completed_tasks.append(task)
            tasks.pop(task_number - 1)
            print("Task completed!")
        else:
            print("Task already completed!")
    else:
        print("Invalid task number. Please enter a valid task number")

def delete_tasks(tasks):
    # delete task - function to enter the task number and remove from list
    view_tasks(tasks)
    task_number = int(input("Enter task number you want to delete: "))

    # check task number to delete task or not
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number. PLease enter a valid task number")
        pass
    pass

def to_do_list():
    # create empty lists to store tasks and completed tasks
    tasks = []
    completed_tasks = []

    # input name from user
    name = input("Enter your name: ")

    while True:
        # display menu
        print("\n** ** To Do List Menu ** **\n")
        print("Welcome,", name, "\n")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit\n")

        choice = input("Enter your choice (1 - 5): ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            marked_tasks(tasks, completed_tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            # break the loop
            print("Thanks for using this program\n")
            break
        else:
            # code for invalid input
            print("Invalid choice. Please choose a valid option from 1 to 5\n")

if __name__ == "__main__":
    to_do_list()