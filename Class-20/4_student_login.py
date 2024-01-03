# Function for student login
def student_login():
    attempts_left = 3

    while attempts_left > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "student" and password == "python123":
            print("Login successful! Welcome to the student management website.")
            break
        else:
            attempts_left -= 1
            print(f"Invalid credentials. {attempts_left} attempts left.")

    if attempts_left == 0:
        print("Account locked. Please contact support.")

# Example usage
student_login()
