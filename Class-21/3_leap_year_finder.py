# Leap year finder
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# Example usage
year_to_check = int(input("Enter a year to check for leap year: "))
is_leap_year(year_to_check)
