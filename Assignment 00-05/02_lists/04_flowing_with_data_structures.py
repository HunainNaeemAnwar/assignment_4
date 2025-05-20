# Lesson: Understanding Mutable and Immutable Data Types

# Immutable Data Types (Example: Numbers, Strings)
# - When we modify an immutable data type inside a function, the changes do NOT stay.
# - We must return the value and reassign it to see the changes.

# Mutable Data Types (Example: Lists, Dictionaries)
# - When we modify a mutable data type inside a function, the changes STAY.
# - We do not need to return the value because lists/dictionaries are modified directly.

def add_three_copies(my_list, data):
    for i in range(3):  
        my_list.append(data)
 
def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)  
    add_three_copies(my_list, message)
    print("List after:", my_list) 
    
if __name__ == "__main__":
    main()
