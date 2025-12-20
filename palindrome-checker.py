def PS(s):
    s = s.lower()
    return s == s[::-1]
def PN(num):
    num = str(num)
    return num == num[::-1]

print("PALINDROME CHECKER\n")
while(True):
    print("1.Check String\t 2.Check Number\t 3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        s = input("Enter any string:")
        PS(s)
        if PS(s):
            print("Yes..Its a palindrome")
        else:
            print("No..Its not a palindrome")
    elif choice==2:
        num = input("Enter a number:")
        PN(num)
        if PN(num):
            print("Yes..Its a palindrome")
        else:
            print("No..Its not a palindrome")
    else:
        break


    

