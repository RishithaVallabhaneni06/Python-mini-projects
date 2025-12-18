print("EVEN-ODD & PRIME CHECKER\n")
def even_odd():
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
def prime():
    if num<=1:
        print(num,"is not prime")
        return
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime")
            return
    print(num, "is prime")  
while(True):
    print("1.Want to Check ?\t 2.Exit")
    inp=int(input("Enter your choice:"))
    if inp==1:
        num=int(input("Enter a number:"))
        even_odd()
        prime()
    else:
        break
