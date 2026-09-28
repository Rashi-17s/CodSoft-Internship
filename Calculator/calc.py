
print("===================================")
print("            CALCULATOR"             )
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


user_input = "yes"

while user_input == "yes":

    print("Print select a operation:\n",
        "1. Addition\n",
        "2. Subtraction\n",
        "3. Multiplication\n",
        "4. Division\n",
        "5. Average")


    try:
        select = int(input("Select a operation from 1,2,3,4,5 : "))

        if(select == 1):
            num1 = float(input("Enter 1st number"))
            num2 = float(input("Enter 2nd number"))
            print( num1, "+", num2, "=", addition(num1,num2))
    
        elif(select == 2):
            num1 = float(input("Enter 1st number"))
            num2 = float(input("Enter 2nd number"))
            print( num1, "-", num2, "=", subtraction(num1,num2))
    
        elif(select == 3):
            num1 = float(input("Enter 1st number"))
            num2 = float(input("Enter 2nd number"))
            print(num1, "*", num2, "=", multiplication(num1,num2))
    
        elif(select == 4):
            num1 = float(input("Enter 1st number"))
            num2 = float(input("Enter 2nd number"))
            print(num1, "/", num2, "=", division(num1,num2))
    
        elif(select == 5):
            num1 = float(input("Enter 1st number"))
            num2 = float(input("Enter 2nd number"))
            print("(",num1, "+", num2,")", "/", "2", "=", average(num1,num2))
    
        else:
            print("invalid choice")



    except ValueError:
        print("Please enter numbers only")

    except ZeroDivisionError:
        print("Can't divide by zero")
        
    user_input = input("\nDo you want another calculation (yes,no)").strip().lower()
