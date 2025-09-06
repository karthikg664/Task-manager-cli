def add(task):
    name = input("Enter task name: ")
    status = input("Enter task status( complete / in progress / incomplete ) : ")
    per = float(input("Enter task percentage: "))
    priority = input("Enter task priority (high / medium / low): ")
    task.append(
        {"name": name, "status": status, "percentage": per, "priority": priority}
    )


def view(task):
    print("do you want to see whole list or specific task?")
    choice = input('Enter "Whole" or "Specific": ')
    if choice.lower() == "whole":
        if len(task) > 0:
            for t in task:
                print(f"Task: {task.index(t) + 1}")
                print(f"Name: {t['name']}")
                print(f"Status: {t['status']}")
                print(f"Percentage: {t['percentage']}%")
                print(f"Priority: {t['priority']}")
                print("-" * 20)
            return

        else:
            print("Task not found.")
            print("-" * 20)
            return

    elif choice.lower() == "specific":
        result = True
        name = input("Enter task name: ")
        for t in task:
            if t["name"].lower() == name.lower():
                print(f"Task: {task.index(t) + 1}")
                print(f"Name: {t['name']}")
                print(f"Status: {t['status']}")
                print(f"Percentage: {t['percentage']}%")
                print(f"Priority: {t['priority']}")
                print("-" * 20)
                result = False
                break

        if result:
            print("Task not found.")
            print("-" * 20)
            view(task)

    else:
        print("Invalid choice. Please try again.")
        print("-" * 20)
        view(task)


def update(task):
    print("do you want to update whole list or specific task?")
    choice = input('Enter "Whole" or "Specific": ')
    if choice.lower() == "whole":
        for t in task:
            print(f"Task: {task.index(t) + 1}")
            print(f"Name: {t['name']}")
            print(f"Status: {t['status']}")
            print(f"Percentage: {t['percentage']}%")
            print(f"Priority: {t['priority']}")
            print("-" * 20)

            print("what do you want to update: ")
            update_choice = input("Enter name/status/percentage/priority: ")
            if update_choice.lower() == "name":
                t["name"] = input("Enter new name: ")
            elif update_choice.lower() == "status":
                t["status"] = input("Enter new status: ")
            elif update_choice.lower() == "percentage":
                t["percentage"] = float(input("Enter new percentage: "))
            elif update_choice.lower() == "priority":
                t["priority"] = input("Enter new priority: ")
            else:
                print("Invalid choice. Please try again.")
                continue
        print("All tasks updated successfully.")

    elif choice.lower() == "specific":
        name = input("Enter task name: ")
        result = True
        for t in task:
            if t["name"].lower() == name.lower():
                print(f"Task: {task.index(t) + 1}")
                print(f"Name: {t['name']}")
                print(f"Status: {t['status']}")
                print(f"Percentage: {t['percentage']}%")
                print(f"Priority: {t['priority']}")
                print("-" * 20)

                print("what do you want to update: ")
                update_choice = input("Enter name/status/percentage/priority: ")
                if update_choice.lower() == "name":
                    t["name"] = input("Enter new name: ")
                elif update_choice.lower() == "status":
                    t["status"] = input("Enter new status: ")
                elif update_choice.lower() == "percentage":
                    t["percentage"] = float(input("Enter new percentage: "))
                elif update_choice.lower() == "priority":
                    t["priority"] = input("Enter new priority: ")
                else:
                    print("Invalid choice. Please try again.")
                    
                result = False
                print("Tasks updated successfully.")
        
        if result:
            print("No tasks were updated.")
            print("-" * 20)
            return

    else:
        print("Invalid choice. Please try again.")
        print("-" * 20)
        return


#         for t in task:
#             print("what do you want to update: ")
#             update_choice = input("Enter name/status/percentage/priority: ")
#             if update_choice.lower() == "name":
#                 t["name"] = input("Enter new name: ")

#             elif update_choice.lower() == "status":
#                 t["status"] = input("Enter new status: ")

#             elif update_choice.lower() == "percentage":
#                 t["percentage"] = input("Enter new percentage: ")

#             elif update_choice.lower() == "priority":
#                 t["priority"] = input("Enter new priority: ")

#             else:
#                 print("Invalid choice. Please try again.")
#                 continue

#     elif choice.lower() == "specific":
#         choice = input("Enter task name:")
#         result = True
#         for t in task:
#             if t["name"].lower() == choice.lower():
#                 print("what do you want to update: ")
#                 update_choice = input("Enter name/status/percentage/priority: ")
#                 if update_choice.lower() == "name":
#                     t["name"] = input("Enter new name: ")

#                 elif update_choice.lower() == "status":
#                     t["status"] = input("Enter new status: ")
#                     if t["status"].lower() not in ["complete","in progress","incomplete"]:
#                         print("Invalid status. Please enter a valid status (complete / in progress / incomplete).")
#                         continue

#                 elif update_choice.lower() == "percentage":
#                     t["percentage"] = input("Enter new percentage: ")
#                     if not (0 <= t["percentage"] <= 100):
#                         print("Invalid percentage. Please enter a valid percentage between 0 and 100.")
#                         continue

#                 elif update_choice.lower() == "priority":
#                     t["priority"] = input("Enter new priority: ")
#                     if t["priority"].lower() not in ["low", "medium", "high"]:
#                         print("Invalid priority. Please enter a valid priority (low / medium / high).")
#                         continue

#                 else:
#                     print("Invalid choice. Please try again.")
#                     continue

#                 result = False
#                 print("Task updated successfully.")
#                 print("-" * 20)
#                 break

#         if result:
#             print("Task not found.")
#             print("-" * 20)
#             return

#     else:
#         print("Invalid choice. Please try again.")
#         print("-" * 20)
#         return


def delete(task):
    print("do you want to delete whole list or specific task?")
    choice = input('Enter "Whole" or "Specific": ')
    if choice.lower() == "whole":
        task.clear()
        print("All tasks deleted successfully.")
        print("-" * 20)
        return

    elif choice.lower() == "specific":
        name = input("Enter task name: ")
        result = True
        for t in task:
            if t["name"].lower() == name.lower():
                task.remove(t)
                print("Task deleted successfully.")
                print("-" * 20)
                result = False
                return

        if result:
            print("Task not found.")
            print("-" * 20)
            return

    else:
        print("Invalid choice. Please try again.")
        print("-" * 20)
        return


def exit():
    quit()


def main():
    task = [
        {
            "name": "Buy groceries",
            "status": "incomplete",
            "percentage": 0,
            "priority": "high",
        },
        {
            "name": "Complete Python assignment",
            "status": "in progress",
            "percentage": 50,
            "priority": "high",
        },
        {
            "name": "Clean the house",
            "status": "incomplete",
            "percentage": 0,
            "priority": "medium",
        },
        {
            "name": "Read a book",
            "status": "incomplete",
            "percentage": 0,
            "priority": "low",
        },
        {
            "name": "Pay bills",
            "status": "complete",
            "percentage": 100,
            "priority": "high",
        },
        {
            "name": "Exercise",
            "status": "in progress",
            "percentage": 30,
            "priority": "medium",
        },
        {
            "name": "Call mom",
            "status": "incomplete",
            "percentage": 0,
            "priority": "high",
        },
        {
            "name": "Schedule appointment",
            "status": "incomplete",
            "percentage": 0,
            "priority": "medium",
        },
        {
            "name": "Organize desk",
            "status": "incomplete",
            "percentage": 0,
            "priority": "low",
        },
        {
            "name": "Prepare presentation",
            "status": "in progress",
            "percentage": 70,
            "priority": "high",
        },
    ]

    while True:
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                add(task)
            case 2:
                view(task)
            case 3:
                update(task)
            case 4:
                delete(task)
            case 5:
                exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
