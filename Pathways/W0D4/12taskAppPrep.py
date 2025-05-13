tasks = []
print('Current tasks:', tasks)

new_task = input('Enter a new task: ')
tasks.append(new_task)
print('Updatd tasks:', tasks)

print("You have", len(tasks), "tasks.")

task_to_remove = input("Enter the task to remove: ")
if task_to_remove in tasks:
    tasks.remove(task_to_remove)
    print("Task removed. Updated tasks:", tasks)
else:
    print("Task not found. Please check the spelling and try again.")
