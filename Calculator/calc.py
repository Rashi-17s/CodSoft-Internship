
print("===================================")
print("       SIMPLE CALCULATOR"           )
print("===================================")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def average(num1, num2):
    return (num1 + num2)/2



print("Print select a operation:\n",
    "1. Addition\n",
    "2. Subtraction\n",
    "3. Multiplication\n",
    "4. Division\n",
    "5. Average")


select = int(input("Select a operation from 1,2,3,4,5 : "))
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(select == 1):
    print( num1, "+", num2, "=", addition(num1,num2))
    
elif(select == 2):
    print( num1, "-", num2, "=", subtraction(num1,num2))
    
elif(select == 3):
    print(num1, "*", num2, "=", multiplication(num1,num2))
    
elif(select == 4):
    print(num1, "/", num2, "=", division(num1,num2))
    
elif(select == 5):
    print("(",num1, "+", num2,")", "/", "2", "=", average(num1,num2))
    
else:
    print("invalid choice! Please select again")
