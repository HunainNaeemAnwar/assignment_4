
loop_break=True
INCHES_PER_FOOT = 12
def feet_to_inches(feet):
    inches = feet * INCHES_PER_FOOT
    return inches

def main():
    global loop_break
    while loop_break:
        try:
            feet=int(input("Enter the number of feet: "))
            inches = feet_to_inches(feet)
            print(f"{feet} feet is equal to {inches} inches.")
            loop_break=False
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()