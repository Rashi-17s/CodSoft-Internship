print("===================================")
print("      TO-DO-LIST APPLICATION       ")
print("===================================")

tasks = []

while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Exit")
    
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
        if(len(tasks) == 0):
            print("No task available to update.")
        
        else:
            print("Your Task List.")
            
            index = 0
            for task in tasks:
                print(index, ".", task)
                index +=1
                
            task_number = int(input("Enter task index to update : "))
            if(0<=task_number <len(tasks)):
                new_task = input("Enter New Task : ")
                tasks[task_number] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task")
    
    elif(choice == "4"):
        print("Thank You for using To-Do List")
        break
    
    else:
        print("Invalid choice! Please try again.")

print("Your To-Do-List is ready!")