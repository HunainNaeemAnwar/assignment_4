def greet(name):
    print("Greetings " + name + "!")

def main():
    try:
        name = input("What's your name? ")
        if not name.strip():  # agar sirf space ya empty input ho
            raise ValueError("Empty name is not allowed.")
        greet(name)
    except Exception as e:
        print("Invalid input:", e)

if __name__ == '__main__':
    main()
