user = int(input("Enter a number: "))
if user%3 ==0 and user % 5 == 0:
    print("FizzBuzz")
elif user % 3 == 0:
    print("Fizz")
elif user % 5 == 0:
    print("Buzz")
else:
    print("Not Divisible by 5 nor 3")
