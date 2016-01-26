
import Movement
import Sensors
import Test

def Main():

    move = Movement()
    sense = Sensors()
    test = Test()
    running = True



    while running: #The main loop that the vehicle will cycle through while running
        input_var = input("Choose an option:"
                      "1.  Move test"
                      "2.  Measure distance "
                      "3.  Distance test")
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
            input_var = input("Choose a side:"
                              "1. Front"
                              "2. Back"
                              "3. Bottom")
            if input_var == 1:
                print 'Distance: %f cm' % sense.read_front()
            if input_var == 2:
                print 'Distance: %f cm' % sense.read_back()
            if input_var == 3:
                print 'Distance: %f cm' % sense.read_bottom()

        if input_var == 3:
            test.WheelsTest()


        break

