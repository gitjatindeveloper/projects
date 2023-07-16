# main program for addition, subtraction, multiplication and division

def calculator():
    # accept input from user
    num_1 = input("Enter First Number: ")
    num_2 = input("Enter Second Number: ")

    # condition for number validation
    if not num_1.isdigit() or not num_2.isdigit():
        print("Invalid input! Please enter valid number")
        exit() # exit the program if number is invalid

    operator_select = input("Enter the operation (+, -, *, /): ")

    # condition for operator validation
    valid_select = ['+', '-', '*', '/']
    if not operator_select in valid_select:
        print("Invalid operator! Please enter valid arithmetic operator")
        exit()

    # condition for zero validation
    if operator_select == "/" and num_2 == 0:
        print("Error! division by zero is not allowed")
        exit()

    # convertiion of string to integer
    num_1 = int(num_1)
    num_2 = int(num_2)

    # condition for arithmetic operators
    result = 0
    if operator_select == "+":
        result = num_1 + num_2
    elif operator_select == "-":
        result = num_1 - num_2
    elif operator_select == "*":
        result = num_1 * num_2
    else:
        result = num_1 / num_2

    # final result
    print("The result of", num_1,"and", num_2,"is", result)

    choice_num = input("Do you wnat to perform another calculation? (y/n): ")
    if choice_num.lower() == 'y':
        calculator()
    else:
        print("Thanks you for using the calculator")

# use of function
calculator()