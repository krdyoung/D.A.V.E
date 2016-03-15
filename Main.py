
import ManualOverride as control
import Auto as automatic

def Main():

    running = True
    override = False

    while running:
        print "1. Manual"
        print "2. Automatic"
        print "3. Exit"

        input_option = input()
        input_option = control.verify_input(input_option)

        if input_option == 1:
            override = True

        if input_option == 2:
            override = False
            automatic.run()

        if input_option == 3:
            return

        if override == True:
            override_selection()

        break

def override_selection():
    print "Choose an option: "
    print "1. Movement"
    print "2. Sensors"
    print "3. Cancel"

    input_option = input()
    input_option = control.verify_input(input_option)

    control.control_choice(input_option)
