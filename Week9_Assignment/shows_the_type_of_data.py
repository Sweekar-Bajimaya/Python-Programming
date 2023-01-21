positive_count = 0
negative_count = 0
while True:
    number = input("Enter an integer value (or 'done' to stop): ")
    if number == 'done':
        break
    try:
        number = int(number)
    except ValueError:
        print("Invalid input, please enter an integer or 'done'")
        continue
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
print("Positive integers entered:", positive_count)
print("Negative integers entered:", negative_count)
