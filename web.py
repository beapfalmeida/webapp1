import streamlit as st
import functions

todos = functions.get_todos()


def add_todos():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My To do App")
st.subheader("This is my to do app")
st.write("This app will increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # true
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo", placeholder="Add new todo",
              on_change=add_todos, key='new_todo') # dúvida on change ?

# st.session_state

# a ordem em que escrevemos o código vai colocar os argumentos por essa ordem na app