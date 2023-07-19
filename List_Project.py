# main program for simple to do list

def add_task(tasks):
    # Function to add a task
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    # Function to view tasks
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("View Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def complete_task(tasks):
    # Function to mark a task as complete and remove it from the tasks list
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task index.")

def remove_task(tasks):
    # Function to remove a task
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to remove: "))
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed!")
    else:
        print("Invalid task index.")

def main():
    # initialize empty list to store tasks
    tasks = []

    # Main program loop
    while True:
        print("\nWelcome\n** To Do List Manager **\n")
        print("1. Add task\n2. View tasks\n3. Mark task as completed\n4. Remove task\n5. Exit\n")

        choice_task = input("Enter your choice (1-5): ")

        if choice_task == '1':
            add_task(tasks)
        elif choice_task == '2':
            view_tasks(tasks)
        elif choice_task == '3':
            complete_task(tasks)
        elif choice_task == '4':
            remove_task(tasks)
        elif choice_task == '5':
            print("\nThank you for using the To Do List Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()