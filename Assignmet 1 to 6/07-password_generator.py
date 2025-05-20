import random

def generate_password(length):
    # Characters set (Uppercase + Lowercase + Digits + Symbols)
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$"

    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

def main():
    print("Simple Password Generator")
    length = int(input("Enter password length: "))
    if length < 4:
        print("Password length should be at least 4 for security.")
        return

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
