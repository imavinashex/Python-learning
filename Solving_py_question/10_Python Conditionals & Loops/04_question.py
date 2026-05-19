# Match Case Statements
#
# 
# question- Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case 

day = int(input("Enter a day number:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Teusday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("nvalid day number! Please enter a number from 1 to 7.")


# Question Solved....///\\\