import json
import argparse
import os

file = "tasks.json"

def load() :
    if not os.path.exists(file):
        return []

    f = open(file, "r")

    if os.path.getsize(file) == 0:
        return []

    return json.load(f)

def add_task(title) :
    tasks = load()
    tasks.append({"id" : len(tasks) + 1,
                  "title" : title,
                  "done" : False
                  })
    f = open(file, "w")
    json.dump(tasks, f)
    f.close()
    
def list_tasks() :
    tasks = load()
    status = "pending"
    if len(tasks) == 0 :
        print("No tasks found")
        
    for i in tasks : 
        if i["done"] == True :
            status = "done"
            
    print(f'{i["id"]}. {i["title"]} [{status}]')



def change_status(tasks_id) :
    tasks = load()
    for i in tasks :
        if i["id"] == tasks_id :
            f = open(file, "w")
            i["done"] = True
            json.dump(tasks, f)
            
    print("ID not found")




def main() :
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest = "command")
    
    subparser.add_parser("add").add_argument("title", type = str)
    subparser.add_parser("list")
    subparser.add_parser("done").add_argument("id", type = int)
    
    args = parser.parse_args()
    
    if args.command == "add" :
        add_task(args.title)
        
    elif args.command == "list" :
        list_tasks()
    elif args.command == "done" :
        change_status(args.id)
        
main()