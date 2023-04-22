# Quiz Game Code (Developed in Sublime Text) :-

import time

# while loop to repeat the program/game if user wants
Continue = True
while Continue == True:
    # if-elif-else statements for starting the game

    # print statement to ask the user if they would like to play the game
    print("Do you want to play the Quiz Game? ")

    # delay of 1 seconds
    time.sleep(1)

    # print statement for blank line
    print()

    # consent variable to store Yes or No i.e. user wants to play or not
    consent = str(input("Enter Yes or No : "))

    # delay of 1 seconds
    time.sleep(1)

    # if statement to account for different ways user can say Yes
    if consent == "Yes" or consent == "yes" or consent == "YES":

        # Blank statement
        print()

        # print statement to welcome user to the game
        print("Welcome to the game :-")

        # delay of 2 seconds
        time.sleep(2)

        # Blank statement
        print()

    # elif statement to account for different ways user can say No
    elif consent == "No" or consent == "no" or consent == "NO":

        # blank statement
        print()

        # quit to exit the program in case user entered No
        quit('That is unfortunate, have a great time!')

        # delay of 2 seconds
        time.sleep(2)

        # else statement to account for a input that is not Yes or No i.e invalid like abc
    else:
        quit("Invalid Input!")

    # ------------------------------------------------------------------------------------------------------------------------------
    # The Questionnaire code block

    # print statement to start the quiz
    print('''There are 5 Questions related to basic Computer Fundamentals and Knowledge, here they come :-''')

    # blank statement
    print()

    # count variable to count the Correct Answers/Current Score of user. Initialized as 0 as Current Score is 0.
    count = 0

    # prints the first question
    print("Q1) What is the full form of CPU?")

    # blank line
    print()

    # AnswerOne variable displays the question and intakes the answer/input of user and ran in an if statement to
    # check validity
    AnswerOne = str(input('Full Form of CPU: '))

    # blank statement
    print()

    # if statement to check AnswerOne, i.e. the different ways to input the correct answer
    if AnswerOne == "Central Processing Unit" or AnswerOne == "central processing unit" or AnswerOne == "CENTRAL PROCESSING UNIT":

        # print statement for correct answer
        print("Correct Answer, Well done!")

        # updating the correct variable to account for the right answer i.e. it goes from 0 to 1
        count += 1

        # blank line
        print()

        # prints the current score
        print("Current Score : " + str(count))

        # blank statement
        print()

    # else statement for incorrect answer displays the current score and incorrect answer message
    else:
        print("Incorrect Answer" + "\n" "Current Score : " + str(count))

    # delay of 1 seconds
    time.sleep(1)

    # AnswerTwo variable displays the question and intakes the answer/input of user and ran in an if statement to
    # check validity
    AnswerTwo = str(input('''Q2) Which of the following is a Output device? 
  
    1) Monitor
    2) Mouse
    3) Keyboard 
  
    Enter the correct option number : '''))

    # blank statement
    print()

    # if statement to check AnswerTwo, i.e. the different ways to input the correct answer
    if AnswerTwo == str("1") or AnswerTwo == str("1)") or AnswerTwo == "Monitor":

        # print statement for correct answer
        print("Correct Answer, Well done!")

        # updating the counter variable to account for the right answer i.e. it goes from 0 to 1 or from 1 to 2 in
        # case AnswerOne is True
        count += 1

        # blank line
        print()

        # prints the current score
        print("Current Score : " + str(count))

        # blank line
        print()

    # else statement for incorrect answer displays the current score and incorrect answer message
    else:
        print("Incorrect Answer" + "\n" "Current Score : " + str(count))

    # delay of 1 seconds
    time.sleep(1)

    # AnswerThree variable displays the question and intakes the answer/input of user and ran in an if statement to
    # check validity
    AnswerThree = str(input("Can you name more than 2 Programming Languages - Yes or No : "))

    # blank line
    print()

    # if statement to check AnswerThree, i.e. the different ways to input the correct answer
    if AnswerThree == "Yes" or AnswerThree == "yes" or AnswerThree == "YES":

        # variable x to store the value of AnswerThree and ran in a function ProgramNames
        x = AnswerThree


        # function ProgramNames has x or AnswerThree as the parameter

        def ProgramNames(x):

            """

            :param x: The answer given by user
            :return: list of programming languages known by user
            """

            # Empty List Initialized to store the programming languages
            list = []

            # User inputs the no of elements or No of programming languages knows
            NoOfElements = int(input("Enter No of Programming Languages you know about : "))

            # blank line
            print()

            if NoOfElements < 3:
                quit("Sorry but that is invalid")

            # for loop to input and append the elements to the list initialized above,runs as many times as there are
            # elements
            for i in range(0, NoOfElements):
                # Elements variable to input the elements one by one via the loop
                Elements = input("Enter Language Name : ")

                # blank line
                print()

                # appends the elements to the list/adds the elements to the list one by one
                list.append(Elements)

            # delay of 1 seconds
            time.sleep(1)

            # print statement to show languages/elements
            print("So the Languages you know are :-" + "\n")

            # prints the list of languages
            print(*list)

            # blank line
            print()


        # call for function ProgramNames/runs the function
        ProgramNames(x)

        # print statement for correct answer
        print("Well done!")

        '''updating the counter variable to account for the right answer i.e. it goes from 0 to 1 or from 1 to 2 in case AnswerOne is True
        or from 2 to 3 in case both AnswerOne and AnswerTwo are correct'''
        count += 1

        # blank line
        print()

        # prints the current score
        print("Current Score : " + str(count))

    # else statement for incorrect answer displays the current score and incorrect answer message
    else:
        print("Unfortunate" + "\n" "Current Score : " + str(count))

    ''' print(*list) returns only the values
    print(*unique)              
    print(*freq)'''

    # delay of 1 seconds
    time.sleep(1)

    # blank statement
    print()

    # prints the fourth question
    print("Q4) What is the full form of GPU?")

    # blank line
    print()

    # AnswerFour varaible displays the question and intakes the answer/input of user and ran in an if statement to check validity
    AnswerFour = str(input('Full Form of GPU: '))

    # blank line
    print()

    # if statement to check AnswerFour, i.e. the different ways to input the correct answer
    if AnswerFour == "Graphics Processing Unit" or AnswerFour == "graphics processing unit" or AnswerFour == "GRAPHICS PROCESSING UNIT":

        # print statement for correct answer
        print("Correct Answer, Well done!")

        '''updating the counter variable to account for the right answer i.e. it goes from 0 to 1 or from 1 to 2 in case AnswerOne is True
     or from 2 to 3 in case both AnswerOne and AnswerTwo are correct and so on'''
        count += 1

        # blank line
        print()

        # prints the current score
        print("Current Score : " + str(count))

    # else statement for incorrect answer displays the current score and incorrect answer message
    else:
        print("Incorrect Answer" + "\n" "Current Score : " + str(count))

    # delay of 1 seconds
    time.sleep(1)

    # blank line
    print()

    # AnswerFive variable displays the question and intakes the answer/input of user and ran in an if statement to check validity
    AnswerFive = str(input('''Q5) Which of the following is a Very High Level Programming Language? 
  
    1) Ruby
    2) C
    3) Python 
  
    Enter the correct option number : '''))

    # blank line
    print()

    # if statement to check AnswerFive i.e. the different ways to input the correct answer
    if AnswerFive == str("3") or AnswerFive == str("3)") or AnswerFive == "Python" or AnswerFive == "python":

        # print statement for correct answer
        print("Correct Answer, Well done!")

        # updating the counter variable to account for the right answer i.e. it goes from 0 to 1 or from 1 to 2 in case AnswerOne is True
        count += 1

        # blank line
        print()

        # prints the current score
        print("Current Score : " + str(count))

    # else statement for incorrect answer displays the current score and incorrect answer message
    else:
        print("Incorrect Answer" + "\n" "Current Score : " + str(count))

    # blank line
    print()

    # if-else statements to display the end game goodbye statements depending on count/score
    if count == 5:
        print("All correct Well done!")
    elif count == 0:
        print(("Time to hit the books"))
    else:
        print("Nice Try you scored {0} out of 5".format(count))

    # blank line
    print()
