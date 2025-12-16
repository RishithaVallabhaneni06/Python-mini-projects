import math
print("CALCULATOR\n")
def Calc():
    print("""1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulus\n 6.Power\n 7.Percentage\n 8.Square\n 9.Square Root\n 10.Round\n""")
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=list(map(int, input("Enter numbers: ").split()))  
        print(sum(a))
    elif choice==2:
        a=list(map(int, input("Enter numbers: ").split()))
        result=a[0]
        for i in a[1:]:
            result -= i
        print(result)
    elif choice==3:
        a=list(map(int, input("Enter numbers: ").split()))
        print(math.prod(a))
    elif choice == 4:
        a = list(map(float, input("Enter numbers: ").split()))
        result = a[0]
        for i in a[1:]:
            if i == 0:
                print("Division by zero is not allowed")
                return
            result /= i
        print("Result =", result)
    elif choice==5:
        a=list(map(int, input("Enter numbers: ").split()))
        result=a[0]
        for i in a[1:]:
            result%=i
        print(result)
    elif choice==6:
        a,b=map(int,input("Enter the base and exponent:").split())
        print(pow(a,b))
    elif choice==7:
        total = float(input("Enter the total value: "))
        percent = float(input("Enter the percentage: "))
        result = (percent / 100) * total
        print(result)
    elif choice==8:
        a=list(map(int,input("Enter numbers: ").split()))
        for i in a[0:]:
            print(pow(i,2))
    elif choice==9:
        a=list(map(int,input("Enter numbers: ").split()))
        for i in a[0:]:
            if i<0:
                print("Enter a positive number:")
                break
            print(math.sqrt(i))
    elif choice==10:
        a=list(map(float,input("Enter numbers: ").split()))
        for i in a[0:]:
            print(round(i))
    else:
        print("Invalid Choice..")
while True:
    print("""
1. Calculate
2. Exit
""")

    inp = int(input("Enter your choice: "))

    if inp == 1:
        Calc()   # calculator menu + operations

    elif inp == 2:
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice, try again.")


        
                
            
        
        
        
        
        
        

        
        
