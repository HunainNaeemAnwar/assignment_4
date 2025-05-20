MAX_LENGTH : int = 3

def shorten(list):
    while len(list) > MAX_LENGTH:
        last_element = list.pop()
        print(last_element)


def get_list():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    list = []
    element = input("Please enter an element of the list or press enter to stop : ")
    while element:
        list.append(element)
        element = input("Please enter an element of the list or press enter to stop : ")
    return list

def main():
    list = get_list()
    print(list)
    shorten(list)
    print(list)


if __name__ == '__main__':
    main()