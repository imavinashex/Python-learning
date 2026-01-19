# String Formatting and f-Strings
# 
# 
# 1. Using format() , create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
# 2. Do the same using f-strings.


name = "john"
age = 25

sentance = "My name is {} and I am {} years old."

print(sentance.format(name,age))


# same but using f-string

print(f"My name is {name} and I am {age} years old.")