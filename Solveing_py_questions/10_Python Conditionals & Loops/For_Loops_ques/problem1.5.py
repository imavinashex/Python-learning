# Write a program that keeps asking the user to enter a password until they
#  enter the correct one.


correct_password = "9090"

p = input("Enter Your Password")

while p != correct_password:
    print("Password Wrong! Try agin.")
    p1 = input("Enter Your Password:")
  
print("Password Valid.")