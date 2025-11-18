#python

num1 = float(input("enter first number: "))

op = input("enter operator (+, -, *, /): ")

num2 = float(input("enter second number: "))

if op == "+":
    print("result:", num1 + num2)

elif op == "-":
    print("result:", num1 - num2)

elif op == "*":
    print("result:", num1 * num2)

elif op == "/":
    print("result:", num1 / num2)

else:
    print("invalid operator")

# I put num1 to represent that that was gonna be a number and not anything else. I used float because of how I understood it being that
# the number you assigned to num1 would stay there until you put a operator and another number. I wanted the script to tell you that
# that was the first number and so you knew what to put. I chose input because it reads a line from input, converts it to a string.
# I used op to represent that there would be an operation next and I used input again because I wanted it to tell you to put an operation.
# I did num2 to represent the second number in the calculator that you would use. I used If because I wanted the script to recognize
# the + whenever it was used and use the function inside the print. I used elif because if it wasnt plus I wanted it to check the next 
# operation and if that wasn't the operation it would go to the next and so on. I used else because I wanted the script to realize if
# none of the operations they used were found the system would print invalid operator.