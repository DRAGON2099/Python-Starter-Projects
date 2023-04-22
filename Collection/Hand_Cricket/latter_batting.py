import batting_wick


def latter_bat(wickets):
    print()
    print("Now the Bowling Side will bat")
    print()
    total_runs = 0
    for i in range(wickets):
        player_name = str(input('Please enter name of batsmen : '))
        total_runs += batting_wick.batting_wicket(player_name)

    print(f"The batting side has scored : {total_runs}")
    return total_runs
