import random

print("Let's play rock paper scissors.")

user_choice = int(input("Choose 1 for rock, 2 for paper and 3 for scissors: "))
computer_choice = random.randint(1, 3)

if user_choice == 1:
    if computer_choice == 1:
        print("You picked rock, Computer also picked rock. It's a draw")
    elif computer_choice == 2:
        print("You picked rock, Computer picked paper. Computer Wins!")
    elif computer_choice == 3:
        print("You picked rock, Computer picked scissors. You Won!")
elif user_choice == 2:
    if computer_choice == 1:
        print("You picked paper, Computer picked rock. You Won!")
    elif computer_choice == 2:
        print("You picked paper, Computer also picked paper. It's a draw")
    elif computer_choice == 3:
        print("You picked paper, Computer picked scissors. You Loose!")
elif user_choice == 3:
    if computer_choice == 1:
        print("You picked scissors, Computer picked rock. You Loose!")
    elif computer_choice == 2:
        print("You picked scissors, Computer picked paper. You Won")
    elif computer_choice == 3:
        print("You picked scissors, Computer also picked scissors. It's a draw")
