import Movement as move

def WheelsTest():

    time = 0

    move.bothForward()

    while time <= 10:
        print(time)
        time.sleep(1)
        time += 1

    move.allStop()


