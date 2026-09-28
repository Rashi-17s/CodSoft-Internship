import tkinter as tk

print("===================================")
print("      TO-DO-LIST APPLICATION       ")
print("===================================")

tasks = []
completed = []
priorities = []

def add_task():
    task = task_entry.get()

    if task == "":
        print("Please enter a task!")
        return
    priority = priority_var.get()
    tasks.append(task)
    completed.append(False)
    priorities.append(priority)
    print("Task added successfully!")
    task_entry.delete(0, tk.END)
    view_tasks()

def view_tasks():
    task_list.delete(0, tk.END)
    print("\nYour Task List")
    if len(tasks) == 0:
        print("No tasks available")
    else:
        index = 0
        for task in tasks:
            if completed[index] == True:
                status = "Completed"
            else:
                status = "Pending"
            print(index, ".", task, "- Priority :", priorities[index], "-", status)
            task_list.insert(tk.END, task)
            index += 1

def update_task():
    selected = task_list.curselection()
    if len(selected) == 0:
        print("Please select a task to update!")
        return
    task_number = selected[0]
    new_task = task_entry.get()

    if new_task == "":
        print("Please enter a new task!")
        return
    tasks[task_number] = new_task
    print("Task updated successfully!")
    task_entry.delete(0, tk.END)
    view_tasks()

def delete_task():
    selected = task_list.curselection()
    if len(selected) == 0:
        print("Please select a task to delete!")
        return
    task_number = selected[0]
    deleted_task = tasks.pop(task_number)
    completed.pop(task_number)
    priorities.pop(task_number)
    print("Task deleted successfully!")
    print(
        "Deleted Task :",
        deleted_task
    )
    view_tasks()

def mark_completed():
    selected = task_list.curselection()
    if len(selected) == 0:
        print("Please select a task!")
        return
    task_number = selected[0]
    completed[task_number] = True
    print("Task marked as completed!")
    view_tasks()

def search_task():
    search = search_entry.get().lower()
    task_list.delete(0, tk.END)
    found = False
    index = 0
    for task in tasks:
        if search in task.lower():
            if completed[index] == True:
                status = "Completed"
            else:
                status = "Pending"
            print(index, ".", task, "- Priority :", priorities[index], "-", status)
            task_list.insert(tk.END, task)
            found = True
        index += 1

    if found == False:
        print("No matching task found!")

def clear_search():
    search_entry.delete(0, tk.END)
    view_tasks()
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("700x600")

title = tk.Label(
    root,
    text="TO-DO LIST APPLICATION",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)

task_label = tk.Label(root, text="Enter Task :", font=("Arial", 12))
task_label.pack()

task_entry = tk.Entry(root, width=45, font=("Arial", 12))
task_entry.pack(pady=5)

priority_label = tk.Label(root, text="Select Priority :", font=("Arial", 12))
priority_label.pack()
priority_var = tk.StringVar()
priority_var.set("Medium")

priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=15)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    width=12,
    command=add_task
)

add_button.grid(
    row=0,
    column=0,
    padx=5
)


view_button = tk.Button(
    button_frame,
    text="View Tasks",
    width=12,
    command=view_tasks
)

view_button.grid(
    row=0,
    column=1,
    padx=5
)


update_button = tk.Button(
    button_frame,
    text="Update Task",
    width=12,
    command=update_task
)

update_button.grid(
    row=0,
    column=2,
    padx=5
)


delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=12,
    command=delete_task
)

delete_button.grid(
    row=0,
    column=3,
    padx=5
)


complete_button = tk.Button(
    button_frame,
    text="Complete",
    width=12,
    command=mark_completed
)

complete_button.grid(
    row=0,
    column=4,
    padx=5
)


search_label = tk.Label(
    root,
    text="Search Task :",
    font=("Arial", 12)
)

search_label.pack()


search_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

search_entry.pack(pady=5)


search_button = tk.Button(
    root,
    text="Search",
    width=12,
    command=search_task
)

search_button.pack(pady=5)


clear_button = tk.Button(
    root,
    text="Clear Search",
    width=12,
    command=clear_search
)

clear_button.pack(pady=5)


list_label = tk.Label(
    root,
    text="Your Tasks",
    font=("Arial", 14, "bold")
)

list_label.pack(pady=10)


task_list = tk.Listbox(
    root,
    width=70,
    height=12,
    font=("Arial", 11)
)

task_list.pack()
root.mainloop()
