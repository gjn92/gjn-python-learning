# list to store the task
tasks = []

# menu to add, view, remove and exit todolist

while True:
    menu = input("Type one of the following: 1. Add Task, 2. View Taks, 3. Remove Tasks, 4. Exit: ")
    if menu == "4":
        print(f"You have exited from the program")
        break # This stops the loop

    elif menu == "3":
        print(tasks)
        td_rm = input("What tasks do you want to remove?: ")
        tasks.remove(td_rm)
        print(f"You have successfully removed {td_rm}")
        print(tasks)

    elif menu == "2":
        print(tasks)

    elif menu == "1":
        add_td = input("What task do you want to add the list: ")
        tasks.append(add_td)
        print(f"You have added {add_td} to the list")
        print(tasks)

    else:
        print("Invalid option, please try again!")




