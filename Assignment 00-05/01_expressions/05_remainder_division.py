loop_break=True
def main():
    global loop_break
    while loop_break:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            remainder = num1 % num2
            #USing floor division operator to get the quotient(only integer part)
            quotient = num1 // num2
            print(f"The Result of {num1} divided by {num2} is {quotient} and the Reminder is {remainder}")
            loop_break=False
        except ValueError:
            print("Invalid input. Please enter valid integers.")    

if __name__=="__main__":
    main()
