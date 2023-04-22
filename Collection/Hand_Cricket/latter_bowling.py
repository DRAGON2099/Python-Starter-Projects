import bowling_wick


def latter_bowl(wickets):
    print()
    print("Now the Batting Side will bowl")
    print()
    total_runs = 0
    for i in range(wickets):
        player_name = str(input('Please enter name of bowler : '))
        total_runs += bowling_wick.bowling_wicket(player_name)

    print(f"The batting side has scored : {total_runs}")
    return total_runs


