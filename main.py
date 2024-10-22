def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file.readlines()
    return todos


user_prompt = "Type add, show, edit, complete or exit: "
while True:
    user_decision = input(user_prompt)
    user_decision = user_decision.strip()
    if user_decision.startswith('add'):
        todos = get_todos()
        todo = user_decision[4:]
        todos.append(todo + '\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif user_decision.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_decision.startswith('edit'):
        try:
            index_task = int(user_decision[5:])
            todos = get_todos()

            new_item = input("Enter a new task: ")
            todos[index_task - 1] = new_item + '\n'

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_decision.startswith('complete'):
        try:
            index_task = int(user_decision[8:])

            todos = get_todos()
            index = index_task - 1
            todo_toremove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"{todo_toremove} was removed from you tasks")
        except IndexError:
            print('Invalid command!')
            continue
    elif user_decision.startswith('exit'):
        break
print("Bye!")
