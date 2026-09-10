"""
Program:            To Do List

Author:             Solomon Umoh


Description:        A program that helps users organize their tasks. 


"""

from pathlib import Path

# dynamically find the exact folder where this script (.py file) lives
SCRIPT_DIR = Path(__file__).parent

# lock the text file path to that exact same folder
TODO_FILE_PATH = SCRIPT_DIR / "todo_list.txt"



# create function to add task to todo list file
def add_task(task_text):
    with open(TODO_FILE_PATH, "a") as todo_file:
        todo_file.write(task_text + "\n") # add a new line after adding task
    print(f"Success: Added '{task_text}' to your list! \n")


# create function to delete task in todo list file
def delete_task(task_number):
    try: 
        # read all current tasks
        with open(TODO_FILE_PATH, "r") as file:
            tasks = file.readlines()

        # check if the number matches a valid task index
        if 1 <= task_number <= len(tasks):

            # remove the task (subtract 1 because python lists start at 0)
            removed_task = tasks.pop(task_number - 1)

            # rewrite the remaining tasks back to the file
            with open(TODO_FILE_PATH, "w") as file:
                file.writelines(tasks)

            print(f"Success: Removed '{removed_task.strip()}' from your list!")

        else:
            print("Error: Invalid task number.")

    except FileNotFoundError: 
        print("Error: No tasks exist yet to delete.")



# welcome users to the program
print("===================== DIGITAL TODO LIST ============================\n")

print("Welcome to the digital todo list app. The right place to stay organized. \n")



# create an infinite loop for menu
while True:
    print("============ MENU =============\n")

    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")
    print("4. Exit\n")


    menu_choice = input("Enter a menu number: ").strip()

    
    if menu_choice == "1":
        # open and read the file safely
        try:
            with open(TODO_FILE_PATH, "r") as read_file:
                #readlines() converts the file into a list of strings
                tasks = read_file.readlines()
        except FileNotFoundError:
            # handle the case where the file hasn't been created yet
            tasks = []


        # check if the list of tasks is empty
        if not tasks:
            print("\nYour to-do list is currently empty!\n")
        else:
            print("\n--------------- List of Current Tasks ------------------")

            # loop through and print each task cleanly
            for index, task in enumerate(tasks, 1):

                # strip() removes the extra "\n" newline character from the file
                print(f"{index}. {task.strip()}")
            print("------------------------------------------------------") 


    elif menu_choice == "2":
        # call add task function here when user choose option 2
        menu_choice = input("Type in your task: ").strip()
        if menu_choice:
            add_task(menu_choice)



    # if the user choice is number 3 do the following 
    elif menu_choice == "3":
        #read tasks first to the user what they delete
        try:
            with open(TODO_FILE_PATH, "r") as read_file: 
                tasks = read_file.readlines()
        except FileNotFoundError:
            tasks = []

        if not tasks: 
            print("\nYour list is empty. There is nothing to delete!")
        else:
            # display the tasks with numbers 
            print("\n--- Select a task number to delete ---") 
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task.strip()}")
            print("--------------------------------------")


            # get user input and handle potential typing errors
            try:
                task_choice = int(input("Enter the number of the task to delete: ")) 
                delete_task(task_choice)
            except ValueError:
                print("Error: Please enter a valid number, not text.")

    # if user decides to quit the program
    elif menu_choice == "4":
        print("Goodbye!")
        break



    






