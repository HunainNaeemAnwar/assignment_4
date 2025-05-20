import random

# Step 1: Word list
words = ['python', 'developer', 'hangman', 'keyboard', 'laptop']

# Step 2: Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

# Step 3: Game loop
while attempts > 0:
    # Step 4: Display current progress
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print("\nWord:", display_word)

    # Step 5: Check if the user has guessed the word
    if all(letter in guessed_letters for letter in word):
        print("You guessed it! You win!")
        break

    # Step 6: Take user input
    guess = input("Guess a letter: ").lower()

    # Step 7: Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Step 8: Update guesses or attempts
    guessed_letters.append(guess)
    if guess not in word:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")
    else:
        print("Good guess!")

# Step 9: If attempts are over
if attempts == 0:
    print("You ran out of attempts!")
    print("The word was:", word)
