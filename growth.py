import streamlit as st

#Project Title
st.title("Growth Mindset App")

#Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

#Sidebar Heading
st.sidebar.header("Manage Your Tasks")

#Text Input Field                  
new_task = st.sidebar.text_input("Add a new task:", placeholder="Enter your task here...")

if st.sidebar.button("Add Task"):
    if new_task.strip():  
        #Use a dictionary to store task and completed status
        st.session_state.tasks.append({"task": new_task, "completed": False})  
        st.success("Task added successfully!")
    else:
        st.warning("Task can't be empty!")

#Display Tasks
st.subheader("Your To-Do List")
if not st.session_state.tasks:
    st.info("No tasks found. Add some tasks to get started!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
        
        #Mark As Complete checkbox
        with col1:
            completed = st.checkbox(
                f"**{task['task']}**", 
                value=task["completed"], 
                key=f"check_{index}"
            )
           
        #Update Task
        with col2:  # Added 'with col2:' to align with the layout
            if st.button("edit", key=f"edit_{index}"):
                new_task = st.text_input("Edit Task", task["task"], key=f'edit_{index}')
                if new_task and st.button("save", key=f'save_{index}'):
                    st.session_state.tasks[index]["task"] = new_task
                    st.experimental_rerun()
      
        #Clear All Tasks
        if st.button("clear all tasks"):
            st.session_state.tasks = []
            st.success("All tasks deleted successfully!")

    #Footer
    st.markdown('---')
    st.caption("Stay Productive & Organized!")