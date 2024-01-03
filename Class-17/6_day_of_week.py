# Finding the day of the week from the date
import datetime

# Input date in the format: Year, Month, Day
input_date = input("Enter a date (YYYY-MM-DD): ")

try:
    # Convert the input string to a datetime object
    date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
    
    # Get the day of the week from the datetime object
    day_of_week = date_object.strftime("%A")
    
    print(f"On {input_date}, it's {day_of_week}.")
except ValueError:
    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
