import random
NUM_SIDES = 6
def dice_simulator():
    """Simulates rolling two dice and prints their total"""
    dice1:int= random.randint(1,NUM_SIDES)
    dice2:int= random.randint(1,NUM_SIDES)
    total:int= dice1 + dice2
    # Here we are creating a variable called dice1 which is a local variable beacuase it is created inside the function and only accessable inside the function
    print(f"The total Of both is {total}")
def  main():
    dice1: int = 10
    print(f"dice1 in main() starts as: {dice1} ")
    dice_simulator()
    dice_simulator()
    dice_simulator()
    print(f"dice1 in main() is:{dice1}")

if __name__ == "__main__":
     main()
