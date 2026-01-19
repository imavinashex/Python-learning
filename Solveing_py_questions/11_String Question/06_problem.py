# 5.String Manipulation Challenges
# 1. Given sentence = "Coding in Python is fun" , replace "fun" with "awesome" and print it.

# 2.Find the index of the word "Python" in sentence .

# 3.Convert the entire sentence to uppercase and print it


sentence = "Coding in Python is fun"

replacefun = sentence.replace("fun","awesome")

print(replacefun)
# method 2
print(sentence.replace("fun","awesome"))

# 2nd question
print(sentence.find("Python"))

# 3rd qestion

print("Uppercase:",sentence.upper())