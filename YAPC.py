#YAPC.py (Yet Another Python Calculator)
firstnumber=int(input("Enter your first number: "))
function=input("Enter the function. Addition,subtraction,multiplication, or division: ").lower() #lowercases the function to read it easier
secondnumber = int(input("Enter the second number: "))

#switch case for the functions!
match function:
    case "addition":
        print(firstnumber,"+",secondnumber,"=",firstnumber+secondnumber)
    case "subtraction":
        print(firstnumber,"-",secondnumber,"=",firstnumber-secondnumber)
    case "division":
        print(firstnumber,"/",secondnumber,"=",firstnumber/secondnumber)
    case "multiplication":
        print(firstnumber,"*",secondnumber,"=",firstnumber*secondnumber)
    case _:
        print("you failed to provide a proper function, goodbye")
