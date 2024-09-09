user_prompt = "Type add, show, edit, complete or exit: "
while True:
    user_decision = input(user_prompt)
    user_decision = user_decision.strip()
    match user_decision:
        case "add":
            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()

            todo = input("Enter a todo: ") +"\n"
            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")

        case "edit":
            index_task = int(input("Index of the task to edit: "))
            new_item = input("Enter a new task: ")
            todos[index_task - 1] = new_item

        case "complete":
            index_task = int(input("Index of the task to mark as completed: "))
            todos.pop(index_task - 1)
        case "exit":
            break
print("Bye!")