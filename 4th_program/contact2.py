tasks = []
while True:
    print("\n1.Add  2.View  3.Delete  4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task)
        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print("Task Added")
    elif ch == 2:
        print(tasks)
    elif ch == 3:
        task = input("Enter task: ")
        if task in tasks:
            tasks.remove(task)
            print("Task Deleted")
    else:
        break