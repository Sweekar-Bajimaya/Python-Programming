temp = int(input("Enter the temperature: "))
hum = int(input("Enter the humidity: "))
if temp >= 85 and hum > 60:
    print("Muggy day today")
elif temp>=85:
    print("warm but not muggy day")
elif temp>=65:
    print("pleasent today")
elif temp>=45:
    print("cold today")
else:
    print("cool today")
