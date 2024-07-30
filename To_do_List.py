class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f'Added task: "{task}"')

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            print(f'Updated task {index + 1} to: "{new_task}"')
        else:
            print(f"Task {index + 1} does not exist.")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f'Task {index + 1} marked as done.')
        else:
            print(f"Task {index + 1} does not exist.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Removed task: "{removed_task["task"]}"')
        else:
            print(f"Task {index + 1} does not exist.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f'{i + 1}. {task["task"]} - {status}')

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Update task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. View tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_done(index)
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
