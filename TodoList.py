import os

#To enter a new task .
def Entertask(tasklist):
        task = input("\nEnter your task : ")
        tasklist.append(task)

#To delete a task .        
def Deletetask(tasklist):
        
        task_to_del = int(input("\nEnter the task number which you want to del : "))
        del tasklist[task_to_del - 1]

#To update a task .        
def Updatetask(tasklist):
       
        task_to_update = int(input("\nEnter the task number which you want to update : "))
        updated_task = input("\nEnter the new task name : ")
        tasklist[task_to_update - 1] = updated_task  
#To display the whole task list .        
def Viewtask(tasklist):
        print("\n      Tasks:      ")
        num=1
        for task in tasklist:
            print("      "+str(num)+") "+task+"      ")
            num=num+1

#To mark as complete a task .
def Completetask(tasklist):
        task_to_mark_complete = int(input("\nEnter the task number which you want to mark as complete : "))
        underline = '✓'
        ty=tasklist[task_to_mark_complete-1]
        marked_text = ty +" "+underline
        tasklist[task_to_mark_complete-1] = marked_text

#To clear the whole task list .       
def Clearlist(tasklist):
        tasklist.clear()
        print("\nList is empty now")
        
is_process_done=False
task_list = []
while not is_process_done:
    
    #Menu section.
    print("\n                   Welcome to TO DO LIST 📋                        ")
    print("_________________________________________________________________")
    print("1) To enter a new task in the list.")
    print("2) To delete a task in the list.")
    print("3) To update a task in the list.")
    print("4) To mark as complete a task in the list.")
    print("5) To clear everything from the list.")
      
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    
    #Shows the tasks.
    Viewtask(task_list)  
    
    #Taking user choice.  
    choice = int(input("\nEnter your choice : "))
    
    #Check the user choice and execute the associate code.
    if choice == 1:
            Entertask(task_list)
    elif choice == 2:
            Deletetask(task_list)
    elif choice == 3:
            Updatetask(task_list)        
    elif choice == 4:
            Completetask(task_list)
    elif choice == 5:
            Clearlist(task_list)
       
    else:
            print("Invalid choice")
            
    #Ask user to continue or not.
    option = input("\nWould you like to continue(yes/no) : ").lower()
    if option == 'no':
        is_process_done = True
    elif option != 'yes' and option != 'no':
        print("\nInvalid option.")
    else:
        #Clear the screen.
         os.system('cls')