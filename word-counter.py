print("WORD COUNTER")
def WC():
    l=[]
    stmt=input("Enter any sentence:")
    l=stmt.split()
    print(l)
    print("Word Count:",len(l))
print("1.Count Words\t 2.Exit")
while(True):
    inp=int(input("Enter you choice:"))
    if inp==1:
        WC()
    elif inp==2:
        print("Thank You !!")
        break
    else:
        print("Invalid Choice")
