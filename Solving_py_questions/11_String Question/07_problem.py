# Bonus Questions
# Write a program that counts how many vowels are in a given string.

# Take a user input string and check if it is a palindrome (same forwards and backwards

# 1st Q

sentence = "Write a program that counts how many vowels are in a given string."
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence:
    if(char in vowels):
        sum += 1

print(f"There are {sum} vowels in sentance")


# 2nd question

string1 = input("Enter a palindrome\n")

if(string1==string1[::-1]):
    print("String is palindrime")
else:
    print("String is not palindrome")