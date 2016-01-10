
import Movement #Class which is responsible handling manual input
import Sensors #Class which controls the ultrasonic sensors

def Main():

    move = Movement() #Assigning all the functions of Movement.py to one variable
    sense = Sensors() #Same as the above but with Sensors.py
    running = True



    while running: #The main loop that the vehicle will cycle through while running
        input_var = input("Choose an option:"
                      "1.  Move test"
                      "2.  Measure distance ")
        if input_var == 1 :
            move.rForward()
            move.lForward()
            move.time.sleep(2)
            move.allStop()
            move.time.sleep(0.5)
            move.rBackward()
            move.lBackward()
            move.time.sleep(2)
            move.allStop()

        if input_var == 2:
            print 'Distance: %f cm' % sense.read_distance()


        break

