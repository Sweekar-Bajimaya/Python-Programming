letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_letters = len(letters)
def welcome():
    print("Welcome! to the Caesar Cipher")
    print("This program ecnrypts and decrypts your text with Caesar Cypher.")

def encrypt(text , key):
    ciphertext = ''
    for letter in text:
        letter = letter.upper()
        if not letter =='':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext , key):
    text = ''
    for letter in ciphertext:
        letter = letter.upper()
        if not letter =='':
            index = letters.find(letter)
            if index == -1:
                text += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                text += letters[new_index]
    return text

def enter_message():
    print("Do you want to encrypt of decrypt? (e/d): ")
    user_input = input()
    if user_input =="e" or user_input == "E":
        print("Encrytion mode is selected!")
        key = int(input('Enter the key (1 through 26): '))
        text = input("Enter the text to encrypt: ")
        ciphertext = encrypt(text, key)
        print(f"Cipher Text: {ciphertext}")

    elif user_input == "d" or user_input == "D":
        print("Decryption mode is selected!")
        key = int(input('Enter the key (1 through 26): '))
        text = input("Enter the text to decrypt: ")
        text = decrypt(text, key)
        print(f"Plain Text: {text}")

    print("Do u want to continue? (yes/no)")
    case = input()
    if case == "YES" or case == "yes":
        enter_message()
    elif case == "NO" or case == "no":
        print("Thank You!")
    else:
        print("Invalid output")
    return case

welcome()
enter_message()



