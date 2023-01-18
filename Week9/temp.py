def temperature():
    temp = float(input("Enter the temperature: "))
    if (temp > 36):
        print("Your temperature is high")
    else:
        if (temp < 36):
            print("Your temperature is low")
        else:
            if (temp == 36):
                print("Your temperature is normal")

temperature()
