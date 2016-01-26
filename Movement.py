import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#19 = IN1
#21 = ENA
#23 = IN2
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#22 = IN3
#24 = ENB
#26 = IN4
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def rForward():
    "R motor forward"
    GPIO.output(21, 1)
    GPIO.output(19, 0)
    GPIO.output(23, 1)

def lForward():
    "L motor forward"
    GPIO.output(24, 1)
    GPIO.output(22, 0)
    GPIO.output(26, 1)

def bothForward():
    "L and R motor forward"
    GPIO.output(21, 1)
    GPIO.output(19, 0)
    GPIO.output(23, 1)

    GPIO.output(24, 1)
    GPIO.output(22, 0)
    GPIO.output(26, 1)

def rBackward():
    "R motor backward"
    GPIO.output(21, 1)
    GPIO.output(19, 1)
    GPIO.output(23, 0)

def lBackward():
    "L motor backward"
    GPIO.output(24, 1)
    GPIO.output(22, 1)
    GPIO.output(26, 0)

def allStop():
    GPIO.output(21, 0)
    GPIO.output(24, 0)

rForward()
lForward()
time.sleep(2)
allStop()
time.sleep(0.5)
rBackward()
lBackward()
time.sleep(2)
allStop()