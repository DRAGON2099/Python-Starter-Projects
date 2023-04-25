import time
import random
import string
from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter Master password : ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# comment out this function after the first use
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def view():

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "Password: ", str(fer.decrypt(passw.encode())))


def enter():
    name = input("Enter Name of Account : ")
    pwd = input("Enter Password : ")

    with open('passwords.txt', 'a') as f:
        f.write("Name of Account : " + name + "\n" + f"Password of {name} Account : " + str(fer.encrypt(pwd.encode())) + "\n")


def generate_password():
    #Password will by default contain letters
    number_choice = input("Do you want to include numbers in the password? (Y/N) : ")
    special_choice = input("Do you want to include special characters in the password? (Y/N) : ")

    letters = string.ascii_letters
    numbers = string.digits
    specials = string.punctuation

    characters = letters
    if number_choice == 'Y' or number_choice == 'Yes' or number_choice == 'YES' or number_choice == 'yes':
        characters += numbers
    if special_choice == 'Y' or special_choice == 'Yes' or special_choice == 'YES' or special_choice == 'yes':
        characters += specials    

    gen_pwd = []
    min_length = int(input("Enter Minimum length of Password needed : "))
    max_length = int(input("Enter Maximum length of Password needed : "))
    length = random.randint(min_length,max_length)
    for idx in range (length):
        element = random.choice(characters)
        gen_pwd.append(element)

    final_pwd = ''
    for i in range (len(gen_pwd)):
        final_pwd = final_pwd + gen_pwd[i]

    return final_pwd    

while True:
    mode = input("Would you like to view existing passwords or enter a new one or have a new one generated or quit" '? (view/enter/generate/quit) : ').lower()
    if mode == 'view' or mode == 'View' or mode == 'VIEW':
        view()
    elif mode == 'enter' or mode == 'Enter' or mode == 'ENTER':
        enter()
    elif mode == 'generate' or mode == 'Generate' or mode == 'GENERATE':
        gener_pwd = generate_password()
        print(f"Generated Password is : {gener_pwd}")
    elif mode == 'quit' or mode == 'Quit' or mode == 'QUIT':
        print("Have a nice day!")
        break
    else:
        print("ERROR! Invalid input!")
        continue
