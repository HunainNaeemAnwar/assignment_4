# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def main():
    list = [] 

    vaule = input("Enter a value: ")  
    while vaule:  
        list.append(vaule) 
        vaule = input("Enter a value: ") 

    print("Here's the list:", list)


if __name__ == '__main__':
    main()