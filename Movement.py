import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#19 = IN1
#23 = IN2
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#22 = IN3
#26 = IN4
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def right_forward():

    GPIO.output(17, 0)
    GPIO.output(22, 1)

    print("Right Forward")

def left_forward():

    GPIO.output(18, 0)
    GPIO.output(24, 1)

    print("Left Forward")

def both_forward():

    GPIO.output(17, 0)
    GPIO.output(22, 1)

    GPIO.output(18, 0)
    GPIO.output(24, 1)

    print("Both Forward")

def right_backward():

    GPIO.output(17, 1)
    GPIO.output(22, 0)

    print("Right Backward")

def left_backward():

    GPIO.output(18, 1)
    GPIO.output(24, 0)

    print("Left Backward")

def both_backward():

    GPIO.output(18, 1)
    GPIO.output(24, 0)

    GPIO.output(17, 1)
    GPIO.output(22, 0)

    print("Both Backward")

def all_stop():
    GPIO.output(27, 0)
    GPIO.output(23, 0)

    print("All Stop")

rForward()
lForward()
time.sleep(2)
allStop()
time.sleep(0.5)
rBackward()
lBackward()
time.sleep(2)
allStop()