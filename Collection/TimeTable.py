import time


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
    print("You will now add classes for monday below :- ")
    pass


def tuesday_class_adder():
    print("You will now add classes for monday below :- ")
    pass


def wednesday_class_adder():
    print("You will now add classes for monday below :- ")
    pass


def thursday_class_adder():
    print("You will now add classes for monday below :- ")
    pass


def friday_class_adder():
    print("You will now add classes for monday below :- ")
    pass


def saturday_class_adder():
    print("You will now add classes for monday below :- ")
    pass


def sunday_class_adder():
    print("You will now add classes for monday below :- ")
    pass


# ------------------------------------------------------------------------------------------------------------
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
