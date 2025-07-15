import json

shabbat_tasks = ["Buying challah", "cooking chamin", "lighting candles", "setting the table", "turning off the phone"]
tasks_performed = [False, False, False, False, False]

def start():
    try:
        global shabbat_tasks, tasks_performed
        with open('shabbat_checklist.txt', 'r') as file:
            file_array = json.load(file)
            shabbat_tasks = file_array[0]
            tasks_performed = file_array[1]
    except:
        pass
    menu()

def menu():
    while True:
        print("menu")
        print("1. View List")
        print("2. Mark Task as Done")
        print("3. Add Task")
        print("4. Remove Task")
        print("5. Save and Exit")
        choice = int(input("Select an option (1-5): "))

        match choice:
            case 1:
                print_shabbat_tasks()
            case 2:
                mark_task_done()
            case 3:
                add_task()
            case 4:
                remove_task()
            case 5:
                save_shabbat_tasks()
                break

def print_shabbat_tasks():
    for i in range(len(shabbat_tasks)):
        print(f"{i + 1} {shabbat_tasks[i]} {'✔️' if tasks_performed[i] else ''}")

def mark_task_done():
    num_task = int(input("Enter the number of the task performed: "))
    tasks_performed[num_task - 1] = True
    for i in range(len(shabbat_tasks)):
        print(f"{shabbat_tasks[i]} {'✔️' if tasks_performed[i] else ''}")

def add_task():
    new_task = input("Enter the task you want to add: ")
    shabbat_tasks.append(new_task)
    tasks_performed.append(False)

def remove_task():
    num_task = int(input("Enter the task number you want to remove: "))
    shabbat_tasks.pop(num_task - 1)
    tasks_performed.pop(num_task - 1)

def save_shabbat_tasks():
    with open("shabbat_checklist.txt", 'w') as file:
        json.dump([shabbat_tasks, tasks_performed], file)



if __name__ == '__main__':
    start()