import random
print("Hello! what is your name?")
myname = input()
print('Well,' + myname + 'I am thinking of a number between 1 to 100.')
def game():
    guesstaken = 0

    number = random.randint(1, 100)

    while guesstaken < 3:
        print("Guess the number: ")
        guess = input()
        guess = int(guess)

        guesstaken +=1

        if guess < number:
            print("Too low!")

        if guess > number:
            print("Too High!")

        if guess == number:
            break

    if guess == number:
        guesstaken = str(guesstaken)
        print('Good job,' + myname + 'You guessed my number in ' + guesstaken + ' Congrats')

    if guess!= number:
        number = str(number)
        print('Nope, the number i was thinking was ' + number)

    print("Do u want to play again? (yes/no)" )

    case = input()
    if case == "Yes" or case == "yes":
        game()
    else:
        if case == "No" or case == "no":
            print("Thank you for playing")
        else:
            print("Invalid output")
game()