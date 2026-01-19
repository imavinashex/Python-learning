'''Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:

1. Both length and width
2. Only length (use default width)

'''

def calculate_area(length, width=10):
    return length * width

print(f"The are of This rectangle is ", {calculate_area(18,20)})
print(calculate_area(18))