
# 📝 To-Do List Application

A simple and interactive **To-Do List Application built using Python and Tkinter**.
This project provides a graphical user interface (GUI) that allows users to create and manage their daily tasks easily.
Users can add tasks, assign priorities, update tasks, delete tasks, mark tasks as completed, and search for tasks.

---

## 📌 Project Overview

The To-Do List Application is a beginner-friendly Python project developed to practice programming concepts through a real-world application.
The application uses **Tkinter** to create a graphical user interface instead of a command-line menu.
Tasks are stored using Python lists while the application is running.

---

## ✨ Features

### ➕ 1. Add Task

Users can enter a task and select its priority.
Available priorities:
- High
- Medium
- Low
The task is added to the task list with a **Pending** status.

---

### 📋 2. View Tasks

Users can view all added tasks in the graphical interface.
Detailed task information is also displayed in the VS Code terminal using normal `print()` statements.
The task information includes:
- Task index
- Task name
- Priority
- Completion status

---

### ✏️ 3. Update Task

Users can select a task from the task list and enter a new task name.
The selected task is then updated.
---

### 🗑️ 4. Delete Task

Users can select a task and delete it from the application.
The task's:
- Name
- Priority
- Completion status
are removed together.

---

### ✅ 5. Mark Task as Completed

Users can select a task and click the **Complete** button.
The selected task is then marked as completed.

---

### 🔍 6. Search Task

Users can search for a task by entering a keyword.
The search is **case-insensitive**.
For example:
```text
python
Python
PYTHON
```
can find the same task.

---

### 🔄 7. Clear Search

The **Clear Search** button removes the search keyword and displays the complete task list again.

---

## 🖥️ Graphical User Interface

The application contains:
- Application title
- Task input field
- Priority selection
- Add Task button
- View Tasks button
- Update Task button
- Delete Task button
- Complete button
- Search field
- Search button
- Clear Search button
- Task list

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🖼️ Tkinter
- 💻 Visual Studio Code
- 🔧 Git
- 🌐 GitHub

---

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:
- Variables
- Lists
- Functions
- `if`, `elif`, and `else`
- `for` loops
- `while` loop through the Tkinter event system
- User input
- String methods
- List methods
- Functions and function calls
- Tkinter GUI programming
- Event-driven programming
- `print()` statements

---

## 📚 Tkinter Concepts Used

The project uses several Tkinter components:

### `Tk()`
Creates the main application window.

### `Label`
Displays text such as headings and instructions.

### `Entry`
Allows the user to enter tasks and search keywords.

### `Button`
Provides buttons for different operations.

### `OptionMenu`
Allows the user to select task priority.

### `Listbox`
Displays the list of tasks.

### `Frame`
Groups related buttons together.

### `StringVar`
Stores the selected priority value.

---

## 📂 Project Structure

```text
To-Do-List/
│
├── main.py
└── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Install Python 3 on your computer.
You can check whether Python is installed by running:

```bash
python --version
```

---

### Step 2: Clone the Repository

Clone the GitHub repository using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

---

### Step 3: Open the Project

Open the project folder in **Visual Studio Code**.

---

### Step 4: Run the Application

Open the VS Code terminal and run:

```bash
python main.py
```

The To-Do List graphical interface will open.

---

## 💡 How the Application Works

### Adding a Task

1. Enter the task in the task input field.
2. Select a priority.
3. Click **Add Task**.
4. The task appears in the task list.

Example:

```text
Complete Python Assignment
Priority: High
Status: Pending
```

---

### Updating a Task

1. Select a task from the list.
2. Enter the new task in the task input field.
3. Click **Update Task**.
4. The selected task is updated.

---

### Deleting a Task

1. Select a task from the list.
2. Click **Delete Task**.
3. The selected task is removed.

---

### Completing a Task

1. Select a task from the list.
2. Click **Complete**.
3. The task status changes to **Completed**.

---

### Searching for a Task

1. Enter a keyword in the search field.
2. Click **Search**.
3. Matching tasks are displayed.
To display all tasks again, click **Clear Search**.

---

## 💻 Example Terminal Output

The application also uses normal `print()` statements to display information in the VS Code terminal.
Example:

```text
===================================
      TO-DO-LIST APPLICATION
===================================

Task added successfully!
Your Task List
0 . Complete Python Assignment - Priority : High - Pending
Task marked as completed!
Your Task List
0 . Complete Python Assignment - Priority : High - Completed
```

---

## 📊 Data Storage

The application currently stores task information using three Python lists:
```python
tasks = []
completed = []
priorities = []
```

### `tasks`

Stores the names of tasks.

### `completed`

Stores the completion status of each task.

### `priorities`

Stores the priority of each task.
The information is connected using the same index.
For example:
```text
tasks[0]
completed[0]
priorities[0]
```
represent information about the same task.

---

## ⚠️ Error Handling

The application checks whether the user has entered or selected the required information.
For example, if the user tries to add an empty task:
```text
Please enter a task!
```
If the user tries to update without selecting a task:
```text
Please select a task to update!
```
If no matching task is found during search:
```text
No matching task found!
```

---

## 🎯 Project Objective

The main objective of this project is to develop a simple task management application using Python and Tkinter while learning how to create a graphical user interface and apply Python programming concepts in a practical project.

---

## 📚 Learning Outcomes

Through this project, I learned how to:
- Create a GUI application using Tkinter.
- Create and use Python functions.
- Store and manage data using lists.
- Handle user input.
- Create buttons and input fields.
- Use a Listbox to display data.
- Implement task searching.
- Implement task updating and deletion.
- Manage task completion status.
- Assign priorities to tasks.
- Use Git and GitHub for version control.

---

## 🚀 Future Improvements

Possible future improvements include:
- 💾 Saving tasks permanently using files or a database
- 🎨 Improving the GUI design
- 📊 Adding task statistics
- 🏷️ Adding task categories
- 🔔 Adding task reminders
- 🌓 Adding Dark Mode

---

## 👩‍💻 Author

**Rashi Singh**
B.Sc. Computer Science Student

---

## 📄 License
This project is created for **educational and internship purposes**.