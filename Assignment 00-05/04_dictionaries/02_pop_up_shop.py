def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruits,price in fruits.items():
        quantity= int(input(f"How many {fruits} do you want to buy : "))
        total_cost += (price * quantity)
    
    print(f"Your total is ${total_cost}" )

if __name__ == '__main__':
    main()