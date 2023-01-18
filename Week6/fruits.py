list = ["A", "B", "C"]
print(list)
user = str(input("Enter a letter: "))
if user not in list:
    print("Wrong input")
else:
    if user == "A":
        print("Apple")
    else:
        if user == "B":
            print("Banana")
        else:
            print("Coconut")



