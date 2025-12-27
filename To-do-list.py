print("SIMPLE TO-DO LIST\n")

task = {}

while True:
    print("1.Add Task\t 2.View Tasks\t 3.Finish Task\t 4.Remove Task\t 5.Exit")
    inp = int(input("Enter your Choice: "))

    if inp == 1:
        name = input("Enter task name: ")
        task[name] = "Pending"
        print("Task Added Successfully")

    elif inp == 2:
        if not task:
            print("No tasks available")
        else:
            for name, status in task.items():
                print(name, "->", status)

    elif inp == 3:
        name = input("Enter task name: ")
        if name in task:
            task[name] = "Finished"
            print("Task marked as Done ✅")
        else:
            print("Task doesn't exist")

    elif inp == 4:
        name = input("Enter task name: ")
        if name in task:
            del task[name]
            print("Task Deleted Successfully")
        else:
            print("Task doesn't exist")

    elif inp == 5:
        print("Thank You ")
        break

    else:
        print("Invalid Choice")
