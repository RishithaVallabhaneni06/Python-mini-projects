import random
guess=random.randint(1,101)
def guess_game(num):
    if num<guess:
        print("Secret Number is greater than",num)
    elif num>guess:
        print("Secret Number is less than",num)
for i in range(1,11):
        num=int(input("Enter any number between 1 to 100:"))
        if guess!=num: 
            guess_game(num)
        else:
            print("You Won !")
            break
else:
    print("You lost!")
    print("The secret number was:", guess)
    
