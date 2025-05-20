def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Error: Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} updated."
    else:
        return "Error: Index out of range."

def slice_list(lst, start, end):
    start = max(0, start)
    end = min(len(lst), end)
    if start > end:
        return []
    return lst[start:end]

def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    while True:
        print("\nCurrent list:", my_list)
        print("Choose operation: access / modify / slice / quit")
        choice = input("Operation: ").strip().lower()

        if choice == 'quit':
            print("Game ended.")
            break

        if choice == 'access':
            idx = int(input("Enter index to access: "))
            print(access_element(my_list, idx))

        elif choice == 'modify':
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(my_list, idx, new_val))

        elif choice == 'slice':
            start_idx = int(input("Enter start index: "))
            end_idx = int(input("Enter end index (exclusive): "))
            sliced = slice_list(my_list, start_idx, end_idx)
            print("Sliced list:", sliced)

        else:
            print("Invalid operation, try again.")

if __name__ == "__main__":
    main()
