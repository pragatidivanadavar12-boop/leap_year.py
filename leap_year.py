def is_leap_year(year):
    if year <= 0:
        raise ValueError("Year must be a positive number")
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def get_result(year):
    if is_leap_year(year):
        return f"{year} is a Leap Year."
    else:
        return f"{year} is Not a Leap Year."
def find_leap_years(start_year, end_year):
    if start_year <= 0 or end_year <= 0:
        raise ValueError("Years must be positive")
    if start_year > end_year:
        raise ValueError("Start year must not exceed end year")
    leap_years = []
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years
def main():
    try:
        year = int(input("Enter a year: "))
        print(get_result(year))
    except ValueError as error:
        print("Invalid input:", error)
print("enter values to check if its leap year or not!")
if __name__ == "__main__":
    main()

