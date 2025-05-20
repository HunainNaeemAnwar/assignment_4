def guess_user_number():
    print("Think of a number between 1 and 100 (don't tell me!).")
    print("I will try to guess it.")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"I guessed it in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please enter 'h' for too high, 'l' for too low, or 'c' for correct.")

        if low > high:
            print("Hmm, something doesn’t add up. Are you sure about your answers?")
            break

if __name__ == "__main__":
    guess_user_number()
