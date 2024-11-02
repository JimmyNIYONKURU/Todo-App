import streamlit as st
import func

def add_to_do():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)
    print(todo)

todos = func.get_todos()

st.title("To do app")
st.subheader("This is  NIYONKURU's to do app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Add a new to do...", on_change= add_to_do, key ="new_todo")
