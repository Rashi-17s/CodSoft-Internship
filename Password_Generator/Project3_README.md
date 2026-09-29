
# 🔐 Password Generator

## 📌 Project Description

The **Password Generator** is a Python-based application that generates random passwords according to the user's requirements.
Users can choose the password length and decide whether to include uppercase letters, numbers, and special characters. The program uses Python's `secrets` module to generate passwords securely.

---

## ✨ Features

- Generate random passwords of a user-defined length.
- Include uppercase letters.
- Include numbers.
- Include special characters.
- Always include lowercase letters.
- Ensure at least one character from each selected character category.
- Validate password length and numeric input.
- Generate multiple passwords without restarting the program.
- Use secure random selection with Python's `secrets` module.

---

## 🛠️ Technologies Used

- **Python 3**
- **VS Code** – for writing and running the code.
- **Git and GitHub** – for version control and project storage.

---

## 📚 Python Concepts Used

- **Variables:** Store password length and user choices.
- **While Loop:** Repeat input validation and password generation.
- **If-Else Statements:** Check user selections and password length.
- **Try-Except:** Handle invalid numeric input.
- **Lists:** Store required characters.
- **String Module:** Provide lowercase letters, uppercase letters, digits, and punctuation.
- **Secrets Module:** Select random characters securely.
- **Functions and Methods:** Use methods such as `append()`, `copy()`, `shuffle()`, and `join()`.

---

## 📂 Project Structure

```text
Password-Generator/
│
├── password_generator.py
└── Project3_README.md
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Download the Project

Clone your GitHub repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Open the project folder in VS Code.

### Step 3: Run the Program

Open the terminal and execute:

```bash
python password_generator.py
```

---

## 💻 Application Workflow

1. Enter the desired password length.
2. Choose whether to include uppercase letters.
3. Choose whether to include numbers.
4. Choose whether to include special characters.
5. View the generated password.
6. Choose whether to generate another password.
The program always includes lowercase letters. If an optional character category is selected, the generated password contains at least one character from that category.

---

## 🖥️ Sample Output

```text
===================================
       PASSWORD GENERATOR
===================================

Enter password length: 12

Choose password options:
Include uppercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes

Generated Password: aB7@mK2!pQ9x

Generate another password? (yes/no): no
Thank you for using Password Generator!
```
**Note:** The password shown above is only an example. Your program generates a different random password each time.

---

## ⚠️ Input Validation

The program handles common input errors:
- **Invalid length:** Displays an error if the entered length is not a valid number.
- **Short password:** Requires a minimum password length of 4 characters.
- **Selected character categories:** Includes at least one character from every selected optional category, provided the password length is sufficient.

---

## 🎯 Project Objective

The objective of this project is to learn how to use Python to generate random passwords, accept user preferences, validate input, and work with built-in modules.
It also introduces the `secrets` module, which is designed for generating random values suitable for security-related applications.

---

## 🚀 Future Improvements

- Add a graphical user interface using Tkinter.
- Add an option to exclude similar characters, such as `O` and `0`.
- Add password strength information.
- Allow users to copy the generated password.
- Add more password customization options.

---

## 👩‍💻 Author

**Rashi Singh**  

B.Sc. Computer Science Student

---

## 🎯 Project Goal

The goal of this project is to practise Python programming, conditional statements, loops, exception handling, string manipulation, and secure random password generation while building a useful application.