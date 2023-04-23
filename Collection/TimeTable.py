import time


# ---------------------------------------------------------------------------------------------
# Function to add classes
def class_adder():
    dict = {}
    no_of_classes = int(input("Enter No of Classes for this day : "))
    print()
    for idx in range(no_of_classes):
        class_day = input("Enter Name of Class : ")
        class_duration = input("Enter Timing of Class")

        dict[class_day] = class_duration

    print("So your schedule for that day is :- ")
    print()
    print(dict)
    return dict    


# ---------------------------------------------------------------------------------------------
# Days of the week class checkers

def monday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Monday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Monday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


def tuesday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Tuesday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Tuesday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


def wednesday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Wednesday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Wednesday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


def thursday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Thursday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Thursday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


def friday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Friday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Friday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


def saturday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Saturday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Saturday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


def sunday_classes_checker(x):
    checker = 0
    if x == 'NO' or x == 'no' or x == 'N' or x == 'No':
        print("You have no classes on Sunday!")
        time.sleep(1)
        pass
    elif x == 'YES' or x == 'yes' or x == 'Y' or x == 'Yes':
        print("So you have classes on Sunday")
        time.sleep(1)
        checker = 1
    else:
        print("ERROR! TRY AGAIN!")
    return checker


# ------------------------------------------------------------------------------------------------------------
# Days of the week class adding
def monday_class_adder():
    print("You will now add classes for Monday below :- ")
    class_adder()


def tuesday_class_adder():
    print("You will now add classes for Tuesday below :- ")
    class_adder()


def wednesday_class_adder():
    print("You will now add classes for Wednesday below :- ")
    class_adder()


def thursday_class_adder():
    print("You will now add classes for Thursday below :- ")
    class_adder()


def friday_class_adder():
    print("You will now add classes for Friday below :- ")
    class_adder()


def saturday_class_adder():
    print("You will now add classes for Saturday below :- ")
    class_adder()


def sunday_class_adder():
    print("You will now add classes for Sunday below :- ")
    class_adder()


#--------------------------------------------------------------------------------------------------------
# __main__

print('''Welcome to a Basic Time Table Program. You can view and add classes and timings.''')
print()
time.sleep(0.5)
monday_classes = str(input("Do you have classes on Monday(Y/N) : "))
print()
time.sleep(0.5)
tuesday_classes = str(input("Do you have classes on Tuesday(Y/N) : "))
print()
time.sleep(0.5)
wednesday_classes = str(input("Do you have classes on Wednesday(Y/N) : "))
print()
time.sleep(0.5)
thursday_classes = str(input("Do you have classes on Thursday(Y/N) : "))
print()
time.sleep(0.5)
friday_classes = str(input("Do you have classes on Friday(Y/N) : "))
print()
time.sleep(0.5)
saturday_classes = str(input("Do you have classes on Saturday(Y/N) : "))
print()
time.sleep(0.5)
sunday_classes = str(input("Do you have classes on Sunday(Y/N) : "))
print()
time.sleep(0.5)

monday_class_tf = monday_classes_checker(monday_classes)
tuesday_class_tf = tuesday_classes_checker(tuesday_classes)
wednesday_class_tf = wednesday_classes_checker(wednesday_classes)
thursday_class_tf = thursday_classes_checker(thursday_classes)
friday_class_tf = friday_classes_checker(friday_classes)
saturday_class_tf = saturday_classes_checker(saturday_classes)
sunday_class_tf = sunday_classes_checker(sunday_classes)

if monday_class_tf == 1:
    monday_class_adder()
if tuesday_class_tf == 1:
    tuesday_class_adder()
if wednesday_class_tf == 1:
    wednesday_class_adder()
if thursday_class_tf == 1:
    thursday_class_adder()
if friday_class_tf == 1:
    friday_class_adder()
if saturday_class_tf == 1:
    saturday_class_adder()
if sunday_class_tf == 1:
    sunday_class_adder()
