import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("My Todo App David")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

# st.checkbox("Nakoupit")
# st.checkbox("Vymalovat")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # odstraníme zaškrtnutý úkol z todos.txt
        todos.pop(index)
        functions.write_todos(todos)
        # vymažeme dané todo ze session.state, které je vypsané v prohlížeči
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


# st.session_state