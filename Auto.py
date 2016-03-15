import Movement as move
import Sensors as sense
import time

def Main():

    running = True
    objectDetected = False
    gapDetected = False
    turns_left = 0
    turns_right = 0

    while running:

        move.both_forward()

        while objectDetected == False & gapDetected == False:

            if sense.read_bottom() > 0.75:
                gapDetected = True

            if sense.read_front() < 0.3 & sense.read_back() > 0.01:
                objectDetected = True

        if objectDetected == True:
            if turns_right > turns_left:
                move.right_forward()
                move.left_backward()
                time.sleep(2)
                move.all_stop()
            else:
                move.left_forward()
                move.right_backward()
                time.sleep(2) #
                move.all_stop()

            objectDetected = False

        if gapDetected == True:
            if turns_right > turns_left:
                move.right_forward()
                move.left_backward()
                time.sleep(2)
                move.all_stop()
            else:
                move.left_forward()
                move.right_backward()
                time.sleep(2) #
                move.all_stop()

            gapDetected = False
