class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i + 1}. {task['task']} - {status}")
        else:
            print("No tasks available!")
            
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index!")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index!")

   

def main():
    todo_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1.Display To-Do List")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
             task = input("Enter the task: ")
             todo_list.add_task(task)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.complete_task(index)
        elif choice == "4":
            index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
