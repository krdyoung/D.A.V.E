import Movement as move
import Sensors as sense

def control_choice(input):
    if input == 1:
        control_motors()
    if input == 2:
        control_sensors()
    else:
        return

def control_motors():

    ANGLE_CONSTANT = 0
    MOVEMENT_CONSTANT = 0

    print "Choose and option:"
    print "1. Rotate"
    print "2. Move"
    print "3. Return"

    input_option = input()
    input_option = verify_input(input_option)

    if input_option == 1:
        print "Choose a direction: "
        print "1. Clockwise"
        print "2. Anti-Clockwise"

        input_direction = input()
        input_direction = verify_input(input_direction)

        if input_direction == 1:
            print "Enter the magnitude in degrees: "

            input_magnitude = input()
            verify_input(input_magnitude)

            move.left_forward()
            move.right_backward()

            move.time.sleep(input_magnitude * ANGLE_CONSTANT)

            move.all_stop()
            control_motors()

        if input_direction == 2:
            print "Enter the magnitude in degrees: "

            input_magnitude = input()
            verify_input(input_magnitude)

            move.right_forward()
            move.left_backward()

            move.time.sleep(input_magnitude * ANGLE_CONSTANT)

            move.all_stop()
            control_motors()

        else:
            control_motors()

    if input_option == 2:
        print "Choose an option: "
        print "1. Forwards"
        print "2. Backwards"

        input_direction = input()
        input_direction = verify_input(input_option)

        print "Enter a distance in metres: "

        input_magnitude = input()
        while isinstance(input_magnitude, float) == False & isinstance(input_magnitude, int) == False :
            input_magnitude = input()

        if input_direction == 1:

            move.both_forward()
            move.time.sleep(MOVEMENT_CONSTANT * input_magnitude)

            move.all_stop()
            control_motors()

        if input_direction == 2:

            move.both_backward()
            move.time.sleep(MOVEMENT_CONSTANT * input_magnitude)

            move.all_stop()
            control_motors()

        else:
            control_motors()

    if input_option == 3:
        return

    else:
        control_motors()

def control_sensors():
    print "Choose an option: "
    print "1. Read Measurement"
    print "2. Return"

    input_option = input()
    input_option = verify_input(input_option)

    if input_option == 1:
        print "Enter a time frame in seconds"

        input_magnitude = input()
        input_magnitude = verify_input(input_magnitude)

        for x in range(0 , input_magnitude):
            print "Front Sensor: %fm" % sense.read_front()
            print "Back Sensor: %fm" % sense.read_back()
            print "Bottom Sensor: %fm" % sense.read_bottom()

            move.time.sleep(1)

    if input_option == 2:
        return

def verify_input(variable):
    while isinstance(variable, int) == False:
        variable = input()
    else:
        return variable
