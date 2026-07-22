
from menu import MenuController
from todolist import ToDoList

def main():

    running:bool = True
    task_list:list = []
    menu = MenuController
    todolist = ToDoList

    while(running):
        
        menu.print_menu()
        print("Which option do you want to choose?")
        userinput:int = int(input(">"))

        match userinput:
            case 1:
                print("Type what you want to add to the To-Do List.")
                input = input(">")
                todolist.task_add(userinput)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Exiting the program!")
                running = False
            case __:
                print("Please put in the correct input!")

    
    exit_response = input("...")


main()