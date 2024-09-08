user_prompt = "Type add, show or exit: "
todos = []
while True:
    user_decision = input(user_prompt)
    user_decision = user_decision.strip()
    match user_decision:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            index_task = int(input("What's the index of the task you wanna edit? "))
            new_item = input("Enter a new task: ")
            todos[index_task - 1] = new_item

        case "exit":
            break
print("Bye!")