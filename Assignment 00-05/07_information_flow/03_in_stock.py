def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# Function to check the stock count of specific fruits
def num_in_stock(fruit):
    """
    Returns the number of the specified fruit in stock.
    """
    if fruit == 'apple':
        return 2
    elif fruit == 'durian':
        return 4
    elif fruit == 'pear':
        return 1000
    else:
        return 0

if __name__ == '__main__':
    main()
