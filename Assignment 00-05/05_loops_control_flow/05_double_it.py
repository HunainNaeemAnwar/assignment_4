def main():
    try:
        numm_by_user=int(input("Enter a number : "))
        while numm_by_user <100:
            numm_by_user=numm_by_user*2
            print(numm_by_user)
    except ValueError:
        print(ValueError)

if __name__ == '__main__':
    main()