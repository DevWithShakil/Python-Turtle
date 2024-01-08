# Unique favorite numbers
def unique_favorites(box):
    unique_numbers = list(set(box))
    return unique_numbers

# Example usage
favorite_numbers = [1, 5, 3, 7, 10, 5, 3, 8]
unique_numbers = unique_favorites(favorite_numbers)
print("Unique favorite numbers:", unique_numbers)
