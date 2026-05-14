# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3 ?)


#creating set  

my_set = {1, 2, 3, 3, 4}

print(my_set) # output = {1, 2, 3, 4} set will be automaticly remove dublicate.

# Add 5 to the set, remove 2 , and check if 4 is in the set.

my_set.add(5)
my_set.remove(2)
print(my_set)

#cheking my_set for 4 in present Or Not
if 4 in my_set:
    print("4 in present on set")
else:
    print("4 not in present on set")