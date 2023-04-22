import random


def toss():

    choice = random.randint(1, 2)
    while True:
        user_choice = int(input("Enter 1 for Heads and 2 for Tails : "))

        if user_choice == 1:
            print("So you chose : Heads")
        elif user_choice == 2:
            print("So you chose : Tails")
        else:
            print("ERROR!")
            continue

        if choice == user_choice:
            print("You won the Toss!")
            print()
            toss_return = 'User'
        else:
            print("Cpu won the Toss!")
            print()
            toss_return = 'Cpu'

        return toss_return
