import random


def batting_wicket(a):

    print(f"The one coming onto bat is : {a}")

    run_counter = 0

    while True:

        user_input = int(input("Enter the amount of Runs you want to score (between 1 to 10) : "))

        if (user_input < 1) or (user_input > 10):
            print(f"{user_input} is invalid")
            print("Sorry moving onto next")
            continue

        cpu_input = random.randint(1, 10)

        if user_input == cpu_input:
            print("You are Out!")
            break

        elif user_input != cpu_input:
            print(f"You scored : {user_input}")
            print(f"The bowler had decided to bowl for {cpu_input} runs")
            run_counter += user_input

        else:
            print("ERROR!")

    print(f"In this wicket you scored : {run_counter}")

    return run_counter



