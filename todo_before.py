def todo():
    tasks = []
    while True:
        c = input("1:Add 2:View 3:Quit ")
        if c == '1':
            t = input("Task: ")
            tasks.append(t)
        elif c == '2':
            for i, t in enumerate(tasks):
                print(i+1, t)
        elif c == '3':
            break
