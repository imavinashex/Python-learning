# Create a tuple coordinates = (10, 20) and print both elements.

coordinates = (10,20)

print(coordinates[0]) #output= 10
print(coordinates[1]) #output=2 20



# 2. Try to modify the tuple by setting coordinates[0] = 50 — note what happens.


# coordinates[0] = 50

# print(coordinates) #geting typeerror, tuple object does not support item assigment

# 3. Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.

mylist = list(coordinates) # What I understand first i convert tuple to list then i change the value first element 10 to 50 then i  assigned coordinates to mylist variable then i print mylist 

mylist[0] = 50
coordinates = (mylist)
print(mylist) # output = [50,20]

