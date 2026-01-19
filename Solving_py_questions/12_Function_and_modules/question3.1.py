''' Lambda Functions
1. Write a lambda function that adds two numbers and test it.

2.Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their squares.
'''
# 1st question ans
addition = lambda A: A + A
print(addition(12))

# 2nd question ans

num_list = (1,2,3,4,5)
squares = list(map(lambda A: A**2, num_list))
print(squares)


