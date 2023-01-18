user = input("Enter a character: ")
if user =="a":
    print("b")
elif user == "A":
    print("B")
else:
    a = chr(ord(user)+1)
    print(a)
