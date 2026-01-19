# String Methods and Functions
#  1. Take the string " i love python programming " and:
# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears

qstr = " i love python programming "

rsapece = qstr.strip()
print("Removed extra space:",rsapece)

titlecase = qstr.title()
print("Title case:-",titlecase)

count =  qstr.count("o")
print("Count o:-",count)


# 2. Check if the string "123abc" is alphanumeri.

checkstr = "123bc"

checking = checkstr.isalnum()
print("\nCheck alphanumeric:-",checking)