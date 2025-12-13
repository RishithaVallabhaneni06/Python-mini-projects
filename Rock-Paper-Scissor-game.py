import random
user_Count = 0
computer_Count = 0

def game():
    global user_Count, computer_Count
    choices = ["rock", "paper", "scissors"]

    print("\nWelcome to the Rock-Paper-Scissors Game!")
    print("Instructions: Enter rock, paper, or scissors.\n")

    # Take input
    user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()

    # If no input given, assign a default
    if not user_input:
        print("You did not enter anything! Using default choice: rock")
        user_input = "rock"

    # Validate choice
    if user_input not in choices:
        print("Invalid choice! Using default choice: rock")
        user_input = "rock"
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Winner logic
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        user_Count += 1
    else:
        computer_Count += 1
    print(f"User Count: {user_Count}\tComputer Count: {computer_Count}")

while True:
    game()
    print("\n1. Play Again\t2. Exit")
    inp = input("Enter your choice: ")
    if inp == "2":
        if user_Count>computer_Count:
            print("\nYayy !! User Wins!!")
        else:
            print("Yayy !! Computer Wins!!")
        print("Thanks for playing!") 
        break
