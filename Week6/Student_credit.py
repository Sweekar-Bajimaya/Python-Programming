user = int(input("Enter your credit score: "))
if user>=90:
    print("Senior status")
elif user >=30 and user<60:
    print("Junior")
elif user>=60 and user<90:
    print("Sophomore")
else:
    print("Join the college")
