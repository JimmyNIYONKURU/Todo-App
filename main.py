user_prompt = "Type add, show, edit, complete or exit: "
while True:
    user_decision = input(user_prompt)
    user_decision = user_decision.strip()
    if "add" in user_decision:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo = user_decision[4:] + "\n"
        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif "show" in user_decision:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif "edit" in user_decision:
        index_task = int(user_decision[5:])
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_item = input("Enter a new task: ")
        todos[index_task - 1] = new_item + '\n'

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif "complete" in user_decision:
        index_task = int(user_decision[8:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        index = index_task - 1
        todo_toremove = todos[index].strip('\n')
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        print(f"{todo_toremove} was removed from you tasks")
    elif "exit" in user_decision:
        break
print("Bye!")
