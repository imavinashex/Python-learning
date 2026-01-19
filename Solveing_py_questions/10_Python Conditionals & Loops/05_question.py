# Write a program using match case that simulates a simple calculator.


# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case .


a = float(input("Enter a first number:"))
s = float(input("Enter a second number:"))


op = input("Enter a one of character(+,-,*,/)")

match op:
    case "+":
        print("Result", a+s)
    case "-":
        print("Result",a-s)
    case "*":
        print("Result",a*s)
    case "/":
        if s != 0:
         print("Result",a/s)
        elif s == 0:
            print("You cannot divide with 0")    
    case _:
        print("invalid input")