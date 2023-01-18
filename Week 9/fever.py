def temperature():
    temp = float(input("Enter the temperature: "))
    if (temp < 36):
        print("You temperature is low")
    elif (temp > 36):
        print("Your temperature is high")
    elif (temp == 36):
        print("Your temperature is normal")

temperature()


