# create a list containing the table of 4


table = []
for i in range(1,11):
    table.append(4*i)

print(table)

# another method shortcut

table = [4*i for i in range(1,11)]

print(table)