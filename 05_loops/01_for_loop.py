# examples of "for loop"

# e method example
# range use print table of numbers
# range(start, stop, step) 
# example 1 print number 1 to 10

# for i in range(1, 11):
#     print(i)


# # let's print even numbers from   2 to 20


# for i in range(2, 21):
#        print(i)



# # let's print 2 table using range
# for i in range(2, 21, 2): 
#     print(i)


#  I apply all thing i learn
# making a program to print multiplicato n table of a number entered by user.

num1 = int(input("Enter a number to print its multiplication table;"))
num2 = int(input("Enter a number to print its multiplication table;"))

for i in range(1, 11):
    print(num1,"X",i,"=",num1*i,"\t",num2, "X", i, "=", num2*i)