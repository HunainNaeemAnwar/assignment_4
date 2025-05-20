import math
loop_break=True

def pythagorean_theorem(a, b):
    return math.sqrt(a**2 + b**2)
def main():
    global loop_break
    while loop_break:
        try:
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            c = pythagorean_theorem(a, b)
            print(f"The length of side c is: {c}")
            loop_break=False
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()