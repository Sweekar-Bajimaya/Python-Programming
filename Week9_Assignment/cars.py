import random
cars = ["Bugatti", "Audi", "Ferrari", "BMW", "Mercedes"]
print("The list of cars owned by Sam are: ")
print(cars)
del cars[1]
cars.insert(1, "Lamborghini")
print(cars)
random.shuffle(cars)
print(cars)






