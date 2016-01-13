import time
import RPi.GPIO as GPIO

#Front Sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN)

#Back Sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

#Bottom Sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

def read_front():
    GPIO.output(17, True)
    time.sleep(0.005)
    GPIO.output(17, False)

    while GPIO.input(27) == 0:
        front_signal_off = time.time()

    while GPIO.input(27) == 1:
        front_signal_on = time.time()

    front_time_passed = front_signal_on - front_signal_off
    front_distance = front_time_passed * 17000
    return front_distance

def read_back():
    GPIO.output(5, True)
    time.sleep(0.005)
    GPIO.output(5, False)

    while GPIO.input(6) == 0:
        back_signal_off = time.time()

    while GPIO.input(6) == 1:
        back_signal_on = time.time()

    back_time_passed =  back_signal_on - back_signal_off
    back_distance = back_time_passed * 17000
    return back_distance

def read_bottom():
    GPIO.output(16, True)
    time.sleep(0.005)
    GPIO.output(16, False)

    while GPIO.input(12) == 0:
        bottom_signal_off = time.time()

    while GPIO.input(12) == 1:
        bottom_signal_on = time.time()

    bottom_time_passed = bottom_signal_on - bottom_signal_off
    bottom_distance = bottom_time_passed * 17000
    return bottom_distance
