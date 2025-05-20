import random

options = ["rock", "paper", "scissors"]

user = input("Choose Rock, Paper, or Scissors: ").lower()

computer = random.choice(options)

print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}")

if user == computer:
    print("It's a draw!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")
elif user in options:
    print("Computer wins!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
