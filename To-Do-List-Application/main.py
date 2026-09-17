print("===================================")
print("      TO-DO-LIST APPLICATION       ")
print("===================================")

tasks = []

while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Exit")
    
    choice = input("\nEnter your choice : ")
    
    if(choice == "1"):
        task = input("Enter Your Task : ")
        tasks.append(task)
        print("Task added successfully!")
        
    elif(choice == "2"):
        print("\n Your Task List")
    
        if(len(tasks)==0):
            print("\nNo tasks available")
    
        else:
            number = 1
            for task in tasks:
                print(number, ".", task)
                number += 1
    
    elif(choice == "3"):
        print("Thank You for using To-Do List")
        break
    
    else:
        print("Invalid choice! Please try again.")

print("Your To-Do-List is ready!")