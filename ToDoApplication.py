taskoptions = ["Add", "View", "Delete", "Quit"]
print("Welcome to your To Do List! Here are your options:")
tasklist = []

def add_tasks(tasklist):
    taskadd = input("Type your task to insert into list: ")
    tasklist.append(taskadd)
    print("Adding Task!!!")
    main()  

def view_tasks(tasklist):
    if len(tasklist) == 0:
        print("Your task list is empty!")
    else:
        print("Here are your current tasks: ")
        for number, name in enumerate(tasklist, 1):
            print(f"{number}. {name}")
    main()  

def delete_tasks(tasklist):
    print("Please type the full task you wish to delete:")
    rem = input("Task -> ")
    if rem in tasklist:
        del tasklist[rem] 
        print(f"{rem} has been removed.\n")
    else:
        print(f"{rem} is not in the list.\n")
    main()  

def quit_app():
    print("Quitting To Do app!!")

def main():
    print("Type your desired option: ")
    print(", ".join(map(str, taskoptions)))
    userinput = input("Choose your option: ").lower()
    
    if userinput == "add":
        add_tasks(tasklist)
    elif userinput == "view":
        view_tasks(tasklist)
    elif userinput == "delete":
        delete_tasks(tasklist)
    elif userinput == "quit":
        quit_app()
    else:
        print("Invalid option. Please try again.")
        main()  

main() 