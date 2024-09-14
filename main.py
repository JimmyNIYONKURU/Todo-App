user_prompt = "Type add, show, edit, complete or exit: "
while True:
    user_decision = input(user_prompt)
    user_decision = user_decision.strip()
    match user_decision:
        case "add":
            with open("todos.txt","r") as file:
                todos = file.readlines()

            todo = input("Enter a todo: ") +"\n"
            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)


        case "show":
            with open("todos.txt","r") as file:
                todos = file.readlines()


            #new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}-{item}")

        case "edit":
            index_task = int(input("Index of the task to edit: "))
            with open("todos.txt","r") as file:
                todos = file.readlines()

            new_item = input("Enter a new task: ")
            todos[index_task - 1] = new_item + '\n'

            with open("todos.txt", "w") as file:
                file.writelines(todos)


        case "complete":
            index_task = int(input("Index of the task to mark as completed: "))

            with open("todos.txt","r") as file:
                todos = file.readlines()

            index = index_task - 1
            todo_toremove = todos[index].strip('\n')
            todos.pop()

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"{todo_toremove} was removed from you tasks")
        case "exit":
            break
print("Bye!")