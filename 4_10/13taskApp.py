tasks = []

print("Welcome to the Simple To-Do App!")
print("Type 'quit' at any time to exit")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show all tasks")
    
    choice = input("Enter your choice (1, 2, 3 or 'quit'): ")
    
    if choice == "quit":
        print("Goodbye!")
        break
    
    if choice == "1":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")
    
    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            
            task_num = input("Enter the number of the task to remove: ")
            try:
                task_num = int(task_num)
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed '{removed}'")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")
    
    elif choice == "3":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    
    else:
        print("Invalid choice! Please enter 1, 2, 3 or 'quit'")