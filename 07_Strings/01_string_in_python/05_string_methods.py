# string method 

value1 = "Happy Birthday"

print ( value1.lower())
print ( value1.upper())
print ( value1.split())
print ( value1.strip())
print ( value1.replace("Birthday", "Holi"))

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

# text = "Python is fun and fun and fun"
# print(text.find("is")) # Output: 7 Index of first occurence
# print(text.replace("fun", "awesome")) 

# text = "Apples,Bananas,Pineapples"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Pineapples']))


# text = "Python123"
# print(text.isalpha()) # Output: False
# print(text.isdigit()) # Output: False
# print(text.isalnum()) # Output: True
# print(text.isspace()) # Output: False


# string formatting

name = "imavinashex"
age = 21

print("My name is {} and I am {} year old.".format(name,age))

# using f-string 
print(f"My name is {name} and I am {age} year old.")