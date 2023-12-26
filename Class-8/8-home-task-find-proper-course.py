# Take user input for student information
age = int(input("Enter student's age: "))
grade = float(input("Enter student's grade (0-100): "))
# Determine the course based on age and grade using if-else statements
if age >= 18:
    if grade >= 90:
        course = "English"
    elif 80 <= grade < 90:
        course = "Math"
    else:
        course = "Science"
else:
    if grade >= 90:
        course = "Bengali"
    elif 80 <= grade < 90:
        course = "Social Science"
    else:
        course = "Religion"
        
# Print the recommended course for the student
print(f"Recommended Course: {course}")