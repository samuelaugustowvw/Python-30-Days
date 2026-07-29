import json
import os
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")
def display_menu():
    print("\n========================")
    print("       TO-DO List")
    print("========================")
    print("1 - Add Task")
    print("2 - List Task")
    print("3 - Complete Task")
    print("4 - Remove Task")
    print("0 - Exit")
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
def get_option():
    while True:
        try:
            option = int(input("Choose an option: "))
            if(0<=option<=4):
                return option
        except ValueError:
            print("Invalid number")
def add_task(tasks):
    description = input("Enter the task: ").strip()
    if not description:
        print("Task cannot be empty.")
        return
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print("Task added!")
def list_tasks(tasks):
    if(not tasks):
        print("\nNo tasks yet.")
        return
    print("\n========================")
    print("      Your Tasks")
    print("========================")
    for index, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{index} - [{mark}] {task['description']}")
def choose_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return None
    while True:
        try:
            number = int(input("Task number: "))
            if 1<=number<= len(tasks):
                return number-1 
            print("That number is not in the list.")
        except ValueError:
            print("Please enter a valid number.")
def complete_task(tasks):
    index = choose_task(tasks)
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed!")
def remove_task(tasks):
    index = choose_task(tasks)
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Removed: {removed['description']}")
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        option = get_option()
        match option:
            case 1:
                add_task(tasks)
            case 2:
                list_tasks(tasks)
            case 3:
                complete_task(tasks)
            case 4:
                remove_task(tasks)
            case 0:
                print("\nGoodbye!")
                break
if __name__ == "__main__":
    main()