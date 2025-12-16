print("Multiplication Table Generator")
number=int(input("Enter the number:"))
steps=int(input("Enter the no.of steps:"))
for i in range(1,steps+1):
    print(number,"*",i,"=",number*i)
