import json
import argparse
import os

file = "tasks.json"

def load() :
    if not os.path.exists(file):
        return []

    if os.path.getsize(file) == 0:
        return []
    f = open(file, "r")
    t = json.load(f)
    f.close()
    return t

def add_task(title) :
    tasks = load()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    tasks.append({"id" : new_id,
                  "title" : title,
                  "status" : "to-do"
                  })
    f = open(file, "w")
    json.dump(tasks, f)
    f.close()
    print(f"Task: {title} added successfully")
    
def list_tasks(based_on = None) :
    tasks = load()
    if len(tasks) == 0 :
        print("No tasks found")
        return
        
    if based_on != None :
        tasks = [i for i in tasks if i["status"] == based_on]
        
    if len(tasks) == 0 :
        print("No tasks found !")
        return
        
    for i in tasks : 
         
        print(f'{i["id"]}. {i["title"]} {i["status"]}')


    
def change_status(tasks_id, new_status) :
    tasks = load()
    for i in tasks :
        if i["id"] == tasks_id :
            f = open(file, "w")
            i["status"] = new_status
            json.dump(tasks, f)
            print(f"Success")
            f.close()
            return
            
    print("ID not found")

def delete_task(task_id) :
    tasks = load()
    
    tasks = [i for i in tasks if i["id"] != task_id]
        
    f = open(file, "w")
    json.dump(tasks, f)
    f.close()
    



def main() :
    parser = argparse.ArgumentParser(
        prog = "todo",
        
        description= """
         TASK MANAGER CLI ENGINE
        """,
        
        epilog="""
            QUICK RUN EXAMPLES:
            python todo.py add "Buy groceries"
            python todo.py status 1 in-progress
            python todo.py list --status done
        """
    )
    subparser = parser.add_subparsers(title="AVAILABLE COMMANDS", dest = "command")
    
    
    subparser.add_parser("add", help = "Add new tasks").add_argument("title", type = str)
    # subparser.add_parser("update", help = "Update title of existing task").add_argument("title", type = str)
    subparser.add_parser("delete", help = "Delete an existing task").add_argument("id", type = int)
    
    subparser.add_parser("list-tasks", help = "List all tasks based on their status").add_argument("status", type = str, nargs = "?")
    
    status_parser = subparser.add_parser("change-status")
    status_parser.add_argument("id", type = int)
    status_parser.add_argument("status", type = str)
    
    args = parser.parse_args()
    
    if args.command == "add" :
        add_task(args.title)

    elif args.command == "list-tasks" :
        list_tasks(based_on = args.status)
        
    elif args.command == "change-status" :
        change_status(args.id, args.status)
        
    elif args.command == "delete" :
        delete_task(args.id)
        
main()