# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

def double_of_number(arr):
    for each_index in range(len(arr)):
        element=arr[each_index]
        arr[each_index]=element*2
    return arr
def main():
    arr:list=[1,2,3,4,5,7,8,9]
    print(arr)
    double_of_number(arr)
    print(arr)

if __name__ == "__main__":
    main()