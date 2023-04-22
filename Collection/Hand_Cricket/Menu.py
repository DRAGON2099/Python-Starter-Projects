import initial_batting
import initial_bowling
import time
import toss
import Rules


# ----------------------------------------------------------------------------------------------------------------------

def menu_choices(x):
    if x == 1:
        print("The Toss iss going to start now :- ")
        time.sleep(1)
        toss_result = toss.toss()
        if toss_result == 'User':
            print("You have won the toss!")
            time.sleep(1)
            toss_after_choice = int(input('''Please choose from the following 2 options :-
             1) BAT FIRST
             2) BOWL FIRST'''))
            time.sleep(1)
            if toss_after_choice == 1:
                print("You have chosen to Bat First :- ")
                time.sleep(1)
                wicket_nos = int(input("Please enter the no of wickets you want to play with : "))
                time.sleep(1)
                initial_batting.winner_check(wicket_nos)
            elif toss_after_choice == 2:
                print("You have chosen to Bowl First :- ")
                time.sleep(1)
                wickets_nos = int(input("Please enter the no of wickets you want to play with : "))
                time.sleep(1)
                initial_bowling.winner_check_two(wickets_nos)
            else:
                quit("Invalid Input! Try Again!")
    elif x == 2:
        print("You have chosen to Bat First :- ")
        time.sleep(1)
        wicket_no = int(input("Please enter the no of wickets you want to play with : "))
        time.sleep(1)
        initial_batting.winner_check(wicket_no)
    elif x == 3:
        print("You have chosen to Bowl First :- ")
        time.sleep(1)
        wickets_no = int(input("Please enter the no of wickets you want to play with : "))
        time.sleep(1)
        initial_bowling.winner_check_two(wickets_no)
    elif x == 4:
        Rules.rules()
    elif x == 5:
        quit("Hope You had a Great Time! GoodBye!")


# ---------------------------------------------------------------------------------------------------------------------

print('''Welcome to a simple game of Hand Cricket like back in the day. Please select an option from the menu :-''')
print()
time.sleep(1)
menu_choice = int(input('''1) Initiate Toss
 2) Bat First
 3) Bowl First
 4) Rules
 5) Exit 
 
 Your Choice : '''))

menu_choices(menu_choice)
