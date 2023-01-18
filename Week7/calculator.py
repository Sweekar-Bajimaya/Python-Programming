def calculator():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    list = [1, 2, 3, 4, 5, 6]
    print(list)
    ask = int(input("Enter 1 for add, 2 for subtract, 3 for multiply, 4 for divide, 5 for Truncated dvivision,"
                    "6 for Modulas, 7 for exponentiation: "))
    if ask == 1:
        print("Add: ", (num1+num2))
    elif ask == 2:
        print("Sub: ", (num1-num2))
    elif ask == 3:
        print("Multiply: ", (num1*num2))
    elif ask == 4:
        print("Division: ", (num1/num2))
    elif ask == 5:
        print("Truncated division: ", (num1 // num2))
    elif ask == 6:
        print("Modulas: ", (num1 % num2))
    elif ask == 7:
        print("Exponential: ", (num1 ** num2))
    else:
        print("Invalid Input")
calculator()


