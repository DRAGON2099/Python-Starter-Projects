from playsound import playsound
import time

CLEAR = "\033[2J" 
CLEAR_RETURN = "\033[H"

def alarm(seconds):
    TimeElapsed = 0

    print(CLEAR)

    while TimeElapsed < seconds:
        time.sleep(1)
        TimeElapsed += 1

        TimeLeft = seconds - TimeElapsed
        MinutesLeft = TimeLeft // 60
        SecondsLeft = TimeLeft % 60

        print(CLEAR_RETURN)

        print(f"Alarm will sound in : {MinutesLeft:02d}:{SecondsLeft:02d}")

    playsound("HotWind.mp3")

minutes = int(input("Enter minutes till alarm rings : "))
seconds = int(input("Enter seconds till alarm rings : "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)        
