class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self):
        self.view_tasks()
        if self.tasks:
            task_index = int(input("Enter the index of the task to mark as complete (1, 2, etc.): "))
            if 1 <= task_index <= len(self.tasks):
                completed_task = self.tasks.pop(task_index - 1)
                print(f"Task '{completed_task}' marked as complete!")
            else:
                print("Invalid task index.")
        else:
            print("No tasks available to mark as complete.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.complete_task()
        elif choice == '4':
            print("Thanks for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
