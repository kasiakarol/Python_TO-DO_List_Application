from Art import title

# Function to display all tasks on the list
def display_tasks(tasks_list):
    print("\nTasks on your TO-DO list:")
    for i, task in enumerate(tasks_list, start=1):  # Enumerate function for using both the index and value of the list
        print(f"({i}) {task}")


# Function to display completed tasks on the list
def display_completed_tasks(tasks_list):
    print("\nCompleted tasks on your TO-DO list:")
    for i, task in enumerate(tasks_list, start=1):
        if "■" in task:
            print(f"({i}) {task}")


# Function to display uncompleted tasks on the list
def display_uncompleted_tasks(tasks_list):
    print("\nUncompleted tasks on your TO-DO list:")
    for i, task in enumerate(tasks_list, start=1):
        if "□" in task:
            print(f"({i}) {task}")


# Task list with some initial values for better demonstration
tasks_list = ["Do shopping □", "Exercise □", "Have a coffee □", "Cook dinner □"]

# While loop to enable the user to perform several operations within the same loop
while True:
    try:  # Try block to handle the exceptions such as incorrect input provided by the user or indexation error
        print(title)
        print("List of available actions:\n"
              "(1) Display the list of all your tasks\n"
              "(2) Add a new task\n"
              "(3) Edit a task\n"
              "(4) Delete a task\n"
              "(5) Complete a task\n"
              "(6) Display only completed tasks\n"
              "(7) Display only uncompleted tasks\n"
              "(8) Clear all the tasks\n")

        user_action = input("Choose a number to perform a desired action: ")

        if user_action not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print("Action not found. Please choose 1, 2, 3, 4, 5, 6, 7, or 8.")
        else:
            if user_action == "1":
                display_tasks(tasks_list)

            elif user_action == "2":
                another_task = input("What task do you want to add to the list: ") + " □"
                tasks_list.append(another_task)  # Adding a new task to the tasks_list
                print("\nTask has been added.")
                display_tasks(tasks_list)

            elif user_action == "3":
                display_tasks(tasks_list)

                try:
                    to_edit = int(input("What task do you want to edit: "))
                    if 1 <= to_edit <= len(tasks_list):
                        new_value = input(f"Insert a new value of the task to replace '{tasks_list[to_edit-1]}': ") + " □"
                        tasks_list[to_edit - 1] = new_value  # Editing a specific task from the tasks_list
                        display_tasks(tasks_list)
                    else:
                        print("Invalid task number.")  # Message in case user's input is out of scope of the list
                except ValueError:
                    print("Invalid task number. Please enter a valid integer.")  # Message for invalid input e.g. sting

            elif user_action == "4":
                display_tasks(tasks_list)

                try:
                    to_delete = int(input("What task do you want to delete: "))
                    if 1 <= to_delete <= len(tasks_list):
                        print(f"\nTask '{tasks_list[to_delete-1]}' has been deleted successfully. ")
                        del tasks_list[to_delete - 1]  # Deleting a specific task from the tasks_list
                        display_tasks(tasks_list)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid task number. Please enter a valid integer.")

            elif user_action == "5":
                display_tasks(tasks_list)

                try:
                    to_complete = int(input("What task do you want to mark as completed: "))
                    if 1 <= to_complete <= len(tasks_list):
                        tasks_list[to_complete - 1] = tasks_list[to_complete - 1].replace("□", "■")  # Completing a specific task from the tasks_list
                        print(f"\nTask '{tasks_list[to_complete - 1]}' has been completed. ")
                        display_tasks(tasks_list)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid task number. Please enter a valid integer.")

            elif user_action == "6":
                display_completed_tasks(tasks_list)

            elif user_action == "7":
                display_uncompleted_tasks(tasks_list)

            elif user_action == "8":
                display_tasks(tasks_list)
                if_delete = input("Are you sure you want to delete all the tasks from your list? (Y/N): ")
                if if_delete.upper() == "Y":
                    tasks_list.clear()  # Deleting all the tasks from tasks_list list
                    display_tasks(tasks_list)  # Displaying the empty list to confirm the above action
                else:
                    print("No tasks were deleted.")  # Message in case user didn't confirm the deletion of all the tasks
                    display_tasks(tasks_list)

    except (ValueError, IndexError):
        print("Incorrect value. Try again. ")  # Try except block to print out a message in case of value or index error

    another_action = input("Do you want to perform another action? (Y/N): ")  # To enable user to perform another action
    if another_action.upper() != "Y":
        break
