# Write a function that takes a list of numbers and returns the sum of those numbers.

def arr_sum(arr):
    sum:int=0
    for each_element in arr:
        sum +=each_element
    return sum

def main():
    arr:list=[1,2,3,4,5,7,8,9]
    sum_of_arr:int=arr_sum(arr)
    print(sum_of_arr)

if __name__ == "__main__":
    main()