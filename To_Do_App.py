
# This program manages a To-Do list where users can add, complete, mark, delete, and view tasks.

Flag = True
T_List = []
C_List = []
D_List = []
M_List = []

todo = {"Task":T_List}

while Flag:

    print("\n\t1.Add Task\n\t2.Add Completed Task\n\t3.View Pending Task\n\t4.Mark Task\n\t5.Delete Task\n\t6.View All Task\n\t7.Exit\n")

    choice = int(input("Enter what do you want as number like 1 2.... "))

    if choice == 1:
        count = int(input("Enter how many task you want to add = "))
        for num in range(1,count+1):
            task = input(f"Enter your {len(T_List)+1}st task = ")
            T_List.append(task)
            todo["Task"] = T_List
        print("Task Added...")
        print(todo)

    elif choice == 2:
        completed_task = input("Enter which task is completed = ")

        if completed_task in T_List:
            C_List.append(completed_task)
            todo["Completed Task"] = C_List
            T_List.remove(completed_task)
        print(todo)

    elif choice == 3:
        n = 0
        print("All are pending Task -->\n")
        for p_task in T_List:
            n+=1
            print("\t\t",n,":",p_task)

    elif choice == 4:
        mark_task = input("Enter which task you want mark = ")
        if mark_task in T_List:
            M_List.append(mark_task)
            print(f"Your pending task {mark_task} is marked...!")
        if mark_task in C_List:
            M_List.append(mark_task)
            print(f"Your completed task {mark_task} is marked...!")

    elif choice == 5:
        delete_task = input("Enter which task you want to delete = ")

        if delete_task in M_List and delete_task in T_List:
            print(f"Your mark and pending task {delete_task} is deleted...!")
            T_List.remove(delete_task)
            M_List.remove(delete_task)
        elif delete_task in M_List and delete_task in C_List:
            print(f"Your mark and completed task {delete_task} is deleted...!")
            C_List.remove(delete_task)
            M_List.remove(delete_task)
        elif delete_task in T_List:
            print(f"Your pending task {delete_task} is deleted...!")
            T_List.remove(delete_task)
        elif delete_task in C_List:
            print(f"Your completed task {delete_task} is deleted...!")
            C_List.remove(delete_task)


    elif choice == 6:

        if len(T_List) != 0:
            print("Pending Task: ")
            for p_task in T_List:
                print("\t\t",p_task)
        else:
            print("Not Have Any Pending Task...!")

        if len(C_List) != 0:
            print("Completed Task: ")
            for c_task in C_List:
                print("\t\t",c_task)
        else:
            print("Not Have Any Completed Task...!")

        if len(M_List) != 0:
            print("Mark Task: ")
            for m_task in M_List:
                print("\t\t",m_task)
        else:
            print("Not Have Any Mark Task...!")

    elif choice == 7:
        print("\nThanks And Visit Again...!\n")
        Flag = False