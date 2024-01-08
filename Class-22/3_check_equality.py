# Check equality of two boxes
def are_boxes_equal(box1, box2):
    return set(box1) == set(box2)

# Example usage
box1 = [2, 5, 7, 3, 10]
box2 = [7, 3, 5, 2, 10]
result = are_boxes_equal(box1, box2)

if result:
    print("The two boxes contain equal numbers.")
else:
    print("The two boxes contain different numbers.")
 