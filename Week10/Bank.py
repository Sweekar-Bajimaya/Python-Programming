print("Welcome!")
print("")

def details(string, int, float):
    name = str("Enter your name: ")
    print("Enter your name", name)
    age = int(input("Enter your age: "))
    print("Enter your age: ",age)
    address = input("Enter your address: ")
    print("Enter your address: ",address)
    deposit_amount = float(input("Enter the amount you want to deposit: "))
    print("Enter the amount you want to deposit: ",deposit_amount)

def asking(ask):
    ask = input("Do u want to open an account?(yes/no): ")
    case = input()
    if case == "yes":
        ask.details()
    elif case == "no":
        print("Thank u!")
    else:
        print("Invalid input please try again!")
        ask.asking()
asking('Sweekar')









    # def __init__(self, balance):
    #     self. __balance = balance
    #
    # def deposit (self, amount):
    #     self.__balance +=amount
    #
    # def withdraw(self, amount):
    #     if amount > self.__balance:
    #         raise valueError ()
