from playsound import playsound
import time


def alarm(seconds):
    TimeElapsed = 0

    while TimeElapsed < seconds:
        time.sleep(5)
        TimeElapsed += 1

        TimeLeft = seconds - TimeElapsed
        MinutesLeft = TimeLeft // 60
        SecondsLeft = TimeLeft % 60
