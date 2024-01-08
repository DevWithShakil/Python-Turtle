# School schedule system
def school_schedule(day):
    if day.lower() in ["saturday", "sunday"]:
        print("It's a weekend! No school today.")
    else:
        print("It's a school day. Don't forget to go to school!")

# Example usage
weekday = input("Enter the day of the week: ")
school_schedule(weekday)
