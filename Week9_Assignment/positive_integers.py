total = 0
while True:
    number = int(input("Enter a positive integer: "))

    if number == 100:
        break

    if number < 100:
        total +=number

print("Sum of the integers you have entered is: ",total)


