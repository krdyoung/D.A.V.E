import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

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