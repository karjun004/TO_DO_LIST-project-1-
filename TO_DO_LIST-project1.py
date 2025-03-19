tasks = []  # Empty list to store tasks

def display_menu():
    """Displays the main menu options."""
    print("\n To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    """Adds a new task to the to-do list."""
    task = input("Enter a new task: ").strip()  # Get user input and remove extra spaces
    if task:  # Check if task is not empty
        tasks.append(task)  # Add task to the list
        print(f" Task '{task}' added!")
    else:
        print(" Task cannot be empty.")

def view_tasks():
    """Displays the to-do list."""
    if not tasks:
        print(" No tasks found!")  # Notify user if the list is empty
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, start=1):  # Enumerate for numbered list
            print(f"{i}. {task}")

def delete_task():
    """Deletes a task based on user input."""
    if not tasks:
        print(" No tasks to delete!")  # Notify if there are no tasks
        return  # Exit function if list is empty

    view_tasks()  # Show current tasks before deleting
    
    try:
        index = int(input("Enter task number to delete: ")) - 1  # Convert input to index
        if 0 <= index < len(tasks):  # Check if index is valid
            removed_task = tasks.pop(index)  # Remove task from the list
            print(f" Task '{removed_task}' deleted!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

def main():
    """Main function to run the to-do list program."""
    while True:
        display_menu()  # Show menu options
        choice = input("Choose an option (1-4): ").strip()  # Get user choice

        try:
            choice = int(choice)  # Convert input to an integer

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print(" Exiting To-Do List. Goodbye!")
                break  # Exit the loop to end the program
            else:
                print(" Invalid choice! Please enter a number between 1-4.")

        except ValueError:
            print("Invalid input! Please enter a number (1-4).")

# Run the program
main()
