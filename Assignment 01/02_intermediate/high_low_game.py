import random

NUM_ROUNDS = 5

print("Welcome to the High-Low Game!")
print("--------------------------------")

score = 0

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    

    user_num = random.randint(1, 100)
    comp_num = random.randint(1, 100)

    print(f"Your number is {user_num}")

  
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either higher or lower: ").lower()

   
    result = ""
    if user_num == comp_num:
        result = "Aww, that's incorrect. The computer's number was " + str(comp_num)
    elif guess == "higher" and user_num > comp_num:
        score += 1
        result = "You were right! The computer's number was " + str(comp_num)
    elif guess == "lower" and user_num < comp_num:
        score += 1
        result = "You were right! The computer's number was " + str(comp_num)
    else:
        result = "Aww, that's incorrect. The computer's number was " + str(comp_num)

    print(result)
    print(f"Your score is now {score}\n")

print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
