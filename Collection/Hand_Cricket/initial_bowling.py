import bowling_wick
import latter_batting


def bowling(wickets):
    print(f"So you have decided to play with {wickets} wickets")
    print()
    total_runs = 0
    for i in range(wickets):
        player_name = str(input('Please enter name of bowler : '))
        total_runs += bowling_wick.bowling_wicket(player_name)

    print(f"The batting side has scored : {total_runs}")
    return total_runs


def winner_check_two(wickets):
    batter_runs = bowling(wickets)
    bowler_runs = latter_batting.latter_bat(wickets)
    if batter_runs > bowler_runs:
        difference = batter_runs - bowler_runs
        print(f"Batter Side has won by {difference} Runs!")
    elif batter_runs < bowler_runs:
        diff = bowler_runs - batter_runs
        print(f"Bowler Side has won by {diff} Runs!")
    elif batter_runs == bowler_runs:
        print("It is a TIE!")
    else:
        print("ERROR!")
