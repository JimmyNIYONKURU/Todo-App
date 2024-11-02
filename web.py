import streamlit as st
import func

def add_to_do():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)
    print(todo)

todos = func.get_todos()

st.title("To do app")
st.subheader("This NIYONKURU's to do app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)
st.text_input(label="New To-do", placeholder="Add a new to do...", on_change= add_to_do, key ="new_todo")

print("hello")