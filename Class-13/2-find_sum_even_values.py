# Find the sum of even values from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_even = sum(num for num in numbers if num % 2 == 0)
print(sum_even)
