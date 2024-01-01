# Create a list
fruits = ["apple", "banana", "cherry"]

# Remove a specific value from the list
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]

# Remove the last item from the list
last_fruit = fruits.pop()
print(last_fruit)  # Output: cherry
print(fruits)  # Output: ["apple"]
