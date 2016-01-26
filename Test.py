import Movement
import time

def WheelsTest():

    move = Movement()
    time = 0

    move.bothForward()

    while time <= 10:
        print(time)
        time.sleep(1)
        time += 1

    move.allStop()


