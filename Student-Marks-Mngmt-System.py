print("STUDENTS MARKS MANAGEMENT SYSTEM\n")
store={}
while(True):
    print("1.Add Student Details\t 2.View Student Details\t 3.Calculate total and average\t 4.Delete Student Details 5.Exit\n")
    inp=int(input("Enter your Choice:"))
    if inp==1:
        Roll_No=int(input("Enter Roll No:"))
        n=int(input("How many Subject marks do you want to store:"))
        marks=[]
        for i in range(1,n+1):
            m=int(input(f"Enter marks of Subject {i}: "))
            marks.append(m)
        store[Roll_No]=marks
        print("Student Details added Successfully")
    elif inp==2:
        R=int(input("Enter Roll Number:"))
        if R in store:
            print(store[R])
        else:
            print("Invalid Roll Number")
    elif inp==3:
        R=int(input("Enter Roll Number:"))
        if R in store:
            print("Total :",sum(store[R]))
            print("Average :",sum(store[R])/len(store[R]))
        else:
            print("Invalid Roll Number")
    elif inp==4:
        R=int(input("Enter Roll Number:"))
        if R in store:
            del(store[R])
            print("Student Details deleted Successfully")
        else:
            print("Invalid Roll Number")
    elif inp==5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
    
        
    
    

