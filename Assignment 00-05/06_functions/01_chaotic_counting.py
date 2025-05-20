import random
import time

# Probability of stopping the counting (30% chance)
DONE_LIKELIHOOD = 0.3

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return 
        print(curr_num)
        time.sleep(1)


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
