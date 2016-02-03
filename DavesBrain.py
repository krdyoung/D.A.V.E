import Movement as move
import Sensors as sense
import time

def Main():

    running = True
    objectDetected = False

    while running:

        move.bothForward()

        while objectDetected == False:

            if sense.readFront < 0.3 & sense.readFront > 0.01:
                objectDetected = True

        if objectDetected == True:
            move.lForward()
            move.rBackward()
            time.sleep(2) #
            sense.allStop()
            objectDetected = False


