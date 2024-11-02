import streamlit as st
import func

todos = func.get_todos()

st.title("To do app")
st.subheader("This NIYONKURU's to do app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)
st.text_input(label="", placeholder="Add a new to do...")