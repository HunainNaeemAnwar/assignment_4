import random
NUM_SIDES = 6
def roll_dice():
    dice1:int= random.randint(1,NUM_SIDES)
    dice2:int= random.randint(1,NUM_SIDES)
    print(f"Dice have {NUM_SIDES} sides")
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    total:int= dice1 + dice2
    print(f"The total Of both is {total}")
if __name__ == "__main__":
    roll_dice()