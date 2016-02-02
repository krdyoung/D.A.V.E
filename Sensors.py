import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Front Sensor
GPIO.setup(5, GPIO.OUT) # 17
GPIO.setup(6, GPIO.IN) # 27

#Back Sensor
GPIO.setup(13, GPIO.OUT) # 5
GPIO.setup(19, GPIO.IN) # 6

#Bottom Sensor
GPIO.setup(26, GPIO.OUT) # 16
GPIO.setup(21, GPIO.IN) # 12

def read_front():
    GPIO.output(5, True)
    time.sleep(0.005)
    GPIO.output(5, False)

    while GPIO.input(6) == 0:
        front_signal_off = time.time()

    while GPIO.input(6) == 1:
        front_signal_on = time.time()

    front_time_passed = front_signal_on - front_signal_off
    front_distance = front_time_passed * 170
    return front_distance

def read_back():
    GPIO.output(13, True)
    time.sleep(0.005)
    GPIO.output(13, False)

    while GPIO.input(19) == 0:
        back_signal_off = time.time()

    while GPIO.input(19) == 1:
        back_signal_on = time.time()

    back_time_passed =  back_signal_on - back_signal_off
    back_distance = back_time_passed * 170
    return back_distance

def read_bottom():
    GPIO.output(26, True)
    time.sleep(0.005)
    GPIO.output(26, False)

    while GPIO.input(21) == 0:
        bottom_signal_off = time.time()

    while GPIO.input(21) == 1:
        bottom_signal_on = time.time()

    bottom_time_passed = bottom_signal_on - bottom_signal_off
    bottom_distance = bottom_time_passed * 170
    return bottom_distance
