import random

user_input = input("rock, paper or scissors: ")
user_input = user_input.lower()

choices = [ "rock" , "paper", "scissors"]
computer = random.choice(choices)

print("user choice :",user_input ,", computer choice :", computer)

if user_input == computer:
    print("it's a tie!")

elif user_input == "scissors" and computer == "rock":
    print("computer wins!")

elif user_input == "paper" and computer == "rock":
    print("user wins!")

elif user_input == "scissors" and computer == "paper":
    print("user wins!")

elif user_input == "rock" and computer == "paper":
    print("computer wins!")

elif user_input == "rock" and computer == "scissors":
    print("user wins!")

elif user_input == "paper" and computer == "scissors":
    print("computer wins!")

else:
    print("invalid input!")