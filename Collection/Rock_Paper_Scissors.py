import random

user_wins = 0
cpu_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('''Please Enter the desired option for Rock/Paper/Scissors :-
    
     Rock
    
     Paper
    
     Scissors
    
     Quit Game/q/Q
     
     Enter Your Desired Option : ''').lower()

    print()

    if user_input == 'q':
        print("Hope you had a fun time!")
        break

    if user_input not in options:
        print("Sorry Invalid Input so try again!")
        continue

    cpu_input = random.randint(0, 2)
    # 0 - Rock , 1 - Paper , 2 - Scissors
    cpu_pick = options[cpu_input]
    print(f"CPU picked : {cpu_pick}")

    if user_input == cpu_pick:
        print("Tt is a tie!")

    elif user_input == 'rock' and cpu_pick == 'scissors':
        print("You won!")
        user_wins += 1

    elif user_input == 'scissors' and cpu_pick == 'paper':
        print("You won!")
        user_wins += 1

    elif user_input == 'paper' and cpu_pick == 'rock':
        print("You won!")
        user_wins += 1

    elif user_input == 'rock' and cpu_pick == 'paper':
        print("CPU won!")
        cpu_wins += 1

    elif user_input == 'scissors' and cpu_pick == 'rock':
        print("CPU won!")
        cpu_wins += 1

    elif user_input == 'paper' and cpu_pick == 'scissors':
        print("CPU won!")
        cpu_wins += 1

print(f'''The final scores are as follows :-

    User Score : {user_wins}
    CPU Score : {cpu_wins}
    
    Do play again!''')
