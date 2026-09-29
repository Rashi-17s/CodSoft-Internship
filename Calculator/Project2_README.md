
# 🧮 Calculator

A simple **Python-based Calculator Application** that performs basic mathematical operations through a command-line interface.
The application allows users to perform multiple calculations using two numbers and provides error handling for invalid input and division by zero.

---

## 📌 Project Overview

The Simple Calculator is a beginner-friendly Python project developed to practice functions, conditional statements, loops, user input, and exception handling.
The program displays a menu of operations and calculates the result based on the user's choice.

---

## ✨ Features

### ➕ 1. Addition
Adds two numbers and displays their sum.

### ➖ 2. Subtraction
Subtracts the second number from the first number.

### ✖️ 3. Multiplication
Multiplies two numbers and displays the product.

### ➗ 4. Division
Divides the first number by the second number.

The program handles division by zero using exception handling.

### 📊 5. Average
Calculates the average of two numbers using the formula:

Average = (Number 1 + Number 2) / 2

### 🔄 6. Multiple Calculations
Users can perform multiple calculations without restarting the program.

### ⚠️ 7. Error Handling
The program handles:
- Invalid operation choices
- Non-numeric input
- Division by zero

---

## 🛠️ Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

---

## 🧠 Python Concepts Used

- Variables
- Functions
- Function parameters and return values
- `if`, `elif`, and `else`
- `while` loop
- User input using `input()`
- Output using `print()`
- Type conversion using `int()` and `float()`
- Exception handling using `try` and `except`
- String methods such as `strip()` and `lower()`

---

## 📂 Project Structure

```text
Simple-Calculator/
│
├── calc.py
└── Project2_README.md
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 3: Open the Project

Open the project folder in Visual Studio Code.

### Step 4: Run the Application

Open the terminal and execute:

```bash
python calc.py
```

---

## 📋 Application Menu

```text
===================================
             CALCULATOR
===================================

Print select a operation:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Average
```

---

## 💡 Example

### Example 1: Addition

```text
Select a operation from 1,2,3,4,5 : 1
Enter 1st number: 10
Enter 2nd number: 5
10.0 + 5.0 = 15.0

Do you want another calculation (yes,no): no
```

### Example 2: Multiplication

```text
Select a operation from 1,2,3,4,5 : 3
Enter 1st number: 4
Enter 2nd number: 5
4.0 * 5.0 = 20.0
```

### Example 3: Average

```text
Select a operation from 1,2,3,4,5 : 5
Enter 1st number: 10
Enter 2nd number: 20
( 10.0 + 20.0 ) / 2 = 15.0
```

---

## ⚠️ Error Handling

### Invalid Input

If the user enters text instead of a number:

```text
Please enter numbers only
```

### Invalid Choice

If the user selects an operation outside the available options:

```text
invalid choice
```

### Division by Zero

If the user attempts to divide by zero:

```text
Can't divide by zero
```

---

## 🎯 Project Objective

The objective of this project is to develop a simple calculator using Python and understand how functions, loops, conditional statements, and exception handling work together in a practical application.

---

## 📚 Learning Outcomes

Through this project, I learned how to:
- Create and call Python functions.
- Perform mathematical calculations.
- Accept user input and convert it into numbers.
- Use conditional statements to select operations.
- Use a loop to perform multiple calculations.
- Handle invalid input using exceptions.
- Prevent program crashes caused by division by zero.
- Manage and upload a project using Git and GitHub.

---

## 🚀 Future Improvements

Possible future improvements include:
- Graphical User Interface using Tkinter
- Calculation history
- Percentage calculation
- Power and square root operations
- Improved input validation

---

## 👩‍💻 Author

**Rashi Singh**

B.Sc. Computer Science Student

---

## 📄 License

This project is created for educational and internship purposes.