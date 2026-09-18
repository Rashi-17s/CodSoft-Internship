print("===================================")
print("      TO-DO-LIST APPLICATION       ")
print("===================================")

tasks = []
completed = []

while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    
    choice = input("\nEnter your choice : ")
    
    if(choice == "1"):
        task = input("Enter Your Task : ")
        tasks.append(task)
        completed.append(False)
        print("Task added successfully!")
        
        
    elif(choice == "2"):
        print("\n Your Task List")
    
        if(len(tasks)==0):
            print("\nNo tasks available")
    
        else:
            index = 0
            for task in tasks:
                if(completed[index] == True):
                    status = "Completed"
                else:
                    status = "Pending"
                    
                print(index, ".", task, "-", status)
                index += 1
                
                
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
        if(len(tasks) == 0):
            print("No tasks available to delete")
        else:
            print("Your Task List")
            index = 0
            for task in tasks:
                print(index, ".", task)
                index += 1
                
            task_number = int(input("Enter task index to delete : "))
            if(0<task_number<len(tasks)):
                deleted_task = tasks.pop(task_number)
                completed.pop(task_number)
                print("Task deleted successfully!")
                print("Deleted Task :", deleted_task)
            else:
                print("Invalid task")        
        
    elif(choice == "5"):
        if(len(tasks)==0):
            print("No tasks available")
        else:
            print("Your Task List")
            index = 0
            for task in tasks:
                if(completed[index] == True):
                    status = "Completed"
                else:
                    status = "Pending"
                
                print(index, ".", task, "-", status)
                index += 1
                
            task_number = int(input("Enter task index to mark as completed : "))
            if(0<=task_number<len(tasks)):
                completed[task_number] = True
                print("Task marked as completed!")
            else:
                print("Invalid task index!")
                
                
    elif(choice == "6"):
        print("Thank You for using To-Do List!")
        break
    
    else:
        print("Invalid choice! Please try again.")
