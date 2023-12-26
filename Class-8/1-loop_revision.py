# Loops are used to repeat a specific block of code multiple times. There are two main types of loops: for loops and while loops.

# 1. for Loop:

# The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or objects.

# Example 1:  Range

for i in range(5):
    print(i)


# Example 2: Iterate over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)




# 2. while Loop:

# The while loop is used to repeatedly execute a block of code as long as a condition is true.

# Example: Print Numbers from 1 to 5 using while Loop
num = 1
while num <= 5:
    print(num)
    num += 1
