# What is Match-Case?
#  Match-case is a new feature introduced in Python 3.10 for pattern matching.///\\\
#  It simplifies complex conditional logic.///\\\ its remind me

# syntax of match case

#  status = value
# match status:
#  case pattern1:
#  # Code to execute if value matches pattern1
#  case pattern2:
#  # Code to execute if value matches pattern2
#  case_:
#  # Default case (if no patterns match)

# Example 
server = 404 #  You can change this value get diffrent result.///\\\
match server :
    case 202: #This case match with sever variable is print success massage.///\\\
        print("Success!")
    case  404: #This case match with server variable is print Not Found! massage.///\\\
        print("Not Found!")
    case _: #This case Does"t match with server variable is print Unknown Server Status.///\\\
        print("Unknown Server Status")


print("Program Finised\nThank You Avinash")
