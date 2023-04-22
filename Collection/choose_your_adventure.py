name = str(input("Enter your character name : "))
print(f"Welcome to the game fellow adventurer {name}")

answer = input("You come to a fork in the road with this sense of foreboding... Go left or right? :  ").lower()
if answer == 'left':
    answer_a = input("You find an injured man on the street.... help or ignore? : ").lower()
    if answer_a == 'help':
        print("He hands you a bag of coins, You Win!")
    elif answer_a == 'ignore':
        print("You walk on home as you do everyday...oblivious")
    else:
        quit('Sorry invalid input.... a box drops on your head knocking you out for the bears...You Lose')
elif answer == 'right':
    answer_b = input("You come near a river.... choose to swim or sleep on ground? :")
    if answer_b == 'sleep':
        print("you never wake up but damn those mosquitoes in the night had sharp teeth...You Lose")
    if answer_b == 'swim':
        answer_c = input(
            'This was a good swim and while swimming you wonder how the fish are in the river.... check fish or '
            'ignore? : ').lower()
        if answer_c == 'check':
            print("As you put your face down in the water you look at a titanic snake\'s eyes stare back at you..."
                  "Good Grief")
        elif answer_c == 'ignore':
            print('You go on home wondering why the water felt slick at times...must have been your imagination')
        else:
            quit('Sorry invalid input.... a box drops on your head knocking you out for the bears...You Lose')
    else:
        quit('Sorry invalid input.... a box drops on your head knocking you out for the bears...You Lose')
else:
    quit('Sorry invalid input.... a box drops on your head knocking you out for the bears...You Lose')
