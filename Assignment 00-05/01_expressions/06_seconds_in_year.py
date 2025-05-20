DAYS_IN_YEAR: int = 365
HOURS_IN_DAY: int = 24
MIN_IN_HOUR: int = 60
SEC_IN_MIN: int = 60

def main():
    print(f"There are {DAYS_IN_YEAR * HOURS_IN_DAY * MIN_IN_HOUR * SEC_IN_MIN } seconds in a year!")

if __name__ == '__main__':
    main()