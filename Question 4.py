todo_list = [input("Enter a task to add to the to-do list: ") for _ in range(int(input("Enter number of tasks: ")))]

print("\nTo-Do List:", todo_list)


task_to_remove = input("\nEnter a task to mark as completed: ")
if task_to_remove in todo_list:
    todo_list.remove(task_to_remove)
else:
    print("Task not found.")


print("Updated To-Do List:", todo_list)