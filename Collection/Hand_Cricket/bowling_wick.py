import random


def bowling_wicket(a):
    print(f"The one coming onto bowl is : {a}")

    run_counter = 0

    while True:

        user_input = int(input("Enter the amount of Runs you want to bowl against (between 1 to 10) : "))

        if (user_input < 1) or (user_input > 10):
            print(f"{user_input} is invalid")
            print("Sorry moving onto next")
            continue

        cpu_input = random.randint(1, 10)

        if user_input == cpu_input:
            print("CPU is Out!")
            break

        elif user_input != cpu_input:
            print(f"CPU scored : {cpu_input}")
            run_counter += cpu_input

        else:
            print("ERROR!")

    print(f"In this wicket CPU scored : {run_counter}")

    return run_counter



