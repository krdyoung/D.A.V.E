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



def read_distance():
    GPIO.output(23, True)
    time.sleep(0.005)
    GPIO.output(23, False)

    while GPIO.input(24) == 0:
        signaloff = time.time()

    while GPIO.input(24) == 1:
        signalon = time.time()

    timepassed = signalon - signaloff
    distance = timepassed * 17000
    return distance

while True:
    print 'Distance: %f cm' %read_distance()