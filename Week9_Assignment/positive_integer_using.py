# Initialize a variable to store the sum
total = 0
# Use infinite loop
while True:
    # Get input from the user
    number = input("Enter a positive integer (or 'done' to stop): ")
    if number == 'done':
        break
    # Use try except to check if the entered input is a number
    try:
        number = int(number)
    except ValueError:
        print("Invalid input, please enter a number or 'done'")
        continue
    # check if the entered number is greater than 100
    if number > 100:
        print(f"{number} is greater than 100, it will be excluded")
        continue
    total += number 
# Print the final total
print("Total:", total)
