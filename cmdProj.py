#this is a project that makes a to-do list that uses the command line commands.
#Building a Command Line Application.
#A simple to-do list application that can run in the command line
#Functions of the to-do list are: Add tasks to the list, LIst all the tasks in the list and Remove tasks from the list.
#To add tasks to the list: -a or --add
#To list all the tasks in the list: -l or --list
#To remove tasks from the list: -r or --remove


import os
import argparse

def createParser():
    parser = argparse.ArgumentParser(description="Command Line To-Do list Application")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all the tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser

#function to add tasks to the To-Do list
def addTask(task):
    with open("tasks.txt", 'a') as file:
        file.write(task + "\n")


#function to list all tasks in the To-Do list
def listTasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}: \t {task.strip()}")
    
    else:
        print("No Tasks Found")


#function to remove tasks in the To-Do list
def removeTasks(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()
        with open("tasks.txt", 'w') as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task) 
        print("Task removed successfuly!")
    else:
        print("No tasks Found")

def main():
    parser = createParser()
    args = parser.parse_args()

    if args.add:
        addTask(args.add)
    elif args.list:
        listTasks()
    elif args.remove:
        removeTasks(int(args.remove))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()