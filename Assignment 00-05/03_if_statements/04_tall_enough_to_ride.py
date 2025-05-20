# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

def tall_enough():
    MIN_HEIGHT = 150 
    
    while True:
        try:
            height =int(input("How tall are you: "))  
            if height == "":  
                print("Exiting...")
                break
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input. Please enter a valid height.")

if __name__ == "__main__":
    tall_enough()
