# Speed fine system
def check_speed(speed):
    if speed <= 60:
        print("No fine. Safe speed!")
    elif 61 <= speed <= 70:
        print("200 takas fine. Drive carefully.")
    else:
        print("1000 takas fine. Slow down!")

# Example usage
vehicle_speed = int(input("Enter the speed of the vehicle: "))
check_speed(vehicle_speed)
