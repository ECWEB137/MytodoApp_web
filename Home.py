import streamlit as st
from class_1 import filestuff as fs

todos = fs.loadexisting()

st.set_page_config(layout='wide')

def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    fs.writeChanges(todos)

st.title("My todo App")
st.subheader("This is my todo app")
st.write("this app is to help your <b>productivity</b>", unsafe_allow_html=True)

st.text_input(label="" , placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fs.writeChanges(todos)
        del st.session_state[todo]
        st.rerun()



