# create a program that checks if a person is eligible to vote (age >= 18)

age = input("Enter Your age:")
str_int = int(age)
if(str_int>18):
    print("You are eligible for vote.")
elif(str_int==18):
    
    print("You are eligible for vote.")
elif(str_int<18):
    print("You are not eligible for vote.")
else:
    print("Invalid input.")