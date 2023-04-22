# Code for managing the Password

master_pwd = input("Enter Master password : ")


def view(x):

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)


def enter(x):
    name = input("Enter Name of Account : ")
    pwd = input("Enter Password : ")

    with open('passwords.txt', 'a') as f:
        f.write("Name of Account : " + name + "\n" + f"Password of {name} Account : " + pwd + "\n")


def generate(x):
    pass


while True:
    mode = input("Would you like to view existing passwords or enter a new one or have a new one generated or quit"
                 '? (view/enter/generate/quit) : ').lower()
    if mode == 'view':
        view(1)
    elif mode == 'enter':
        enter(1)
    elif mode == 'generate':
        generate(1)
    elif mode == 'quit':
        print("Have a nice day!")
        break
    else:
        print("Invalid input")
        continue
