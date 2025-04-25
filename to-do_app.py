print("hello world")

def task():
    tasks = []  # List to store tasks
    print("Welcome to the To-Do App!")
    
    total_tasks = int(input("How many tasks do you want to add? "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
        
    print("Your tasks are:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    
    while True:
        operation = int(input("\nEnter:\n1 - To add\n2 - To update\n3 - To delete\n4 - To view\n5 - To exit: "))
        
        if operation == 1:
            add_task = input("Enter the task you want to add: ")
            tasks.append(add_task)
            print(f"Task added successfully: {add_task}")
            
        elif operation == 2:
            update_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= update_index < len(tasks):
                new_task = input("Enter the new task: ")
                tasks[update_index] = new_task
                print(f"Task updated successfully to: {new_task}")
            else:
                print("Invalid task number.")
                
        elif operation == 3:
            delete_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= delete_index < len(tasks):
                removed = tasks.pop(delete_index)
                print(f"Task deleted successfully: {removed}")
            else:
                print("Invalid task number.")
                
        elif operation == 4:
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
                
        elif operation == 5:
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

task()
