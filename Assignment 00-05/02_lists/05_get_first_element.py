
def get_first_element(list):
    """Return the first element of a provided list."""
    try:
        return list[0]
    except IndexError:
        print("List is empty")

def get_list():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    list = []
    element_by_user: str = input("Please enter an element of the list or press enter to stop : ")
    while element_by_user != "":
        list.append(element_by_user)
        element_by_user = input("Please enter an element of the list or press enter to stop : ")
    return list

def main():
    list = get_list()
    print(list)
    first_in_list= get_first_element(list)
    print(first_in_list)
   


if __name__ == '__main__':
    main()

