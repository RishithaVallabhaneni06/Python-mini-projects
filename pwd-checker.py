print("PASSWORD STRENGTH CHECKER")
spl = "#$%^&*"
 
def pwd_checker():
    pwd = input("Enter your password: ")
    score = 0
    if len(pwd) >= 8:
        score += 1
    if any(ch.isupper() for ch in pwd):
        score += 1
    if any(ch.islower() for ch in pwd):
        score += 1
    if any(ch.isdigit() for ch in pwd):
        score += 1
    if any(ch in spl for ch in pwd):
        score += 1
    return score
while True:
    print("\n1. Check password strength\t2. Exit")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        score = pwd_checker()
        if score <= 2:
            print("Weak password ")
        elif score == 3 or score == 4:
            print("Moderate password ")
        else:
            print("Strong password ")
    elif inp == 2:
        print("Thank You !!")
        break
    else:
        print("Invalid choice. Try again.")

