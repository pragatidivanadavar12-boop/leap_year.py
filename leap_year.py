
# Function 1: Check whether a year is a leap year

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Function 2: Display the result

def display_result(year):
    if is_leap_year(year):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")


# Function 3: Main function

def main():
    year = 2024
    print("Leap Year Checking Program")
    display_result(year)


if __name__ == "__main__":
    main()
