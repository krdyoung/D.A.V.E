import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#19 = IN1
#21 = ENA
#23 = IN2
GPIO.setup(17, GPIO.OUT) # 19
GPIO.setup(27, GPIO.OUT) # 21
GPIO.setup(22, GPIO.OUT) # 23

#22 = IN3
#24 = ENB
#26 = IN4
GPIO.setup(18, GPIO.OUT) # 22
GPIO.setup(23, GPIO.OUT) # 24
GPIO.setup(24, GPIO.OUT) # 26

def rForward():

    GPIO.output(27, 1)
    GPIO.output(17, 0)
    GPIO.output(22, 1)

    print("Right Forward")

def lForward():

    GPIO.output(23, 1)
    GPIO.output(18, 0)
    GPIO.output(24, 1)

    print("Left Forward")

def bothForward():

    GPIO.output(27, 1)
    GPIO.output(17, 0)
    GPIO.output(22, 1)

    GPIO.output(23, 1)
    GPIO.output(18, 0)
    GPIO.output(24, 1)

    print("Both Forward")

def rBackward():

    GPIO.output(27, 1)
    GPIO.output(17, 1)
    GPIO.output(22, 0)

    print("Right Backward")

def lBackward():

    GPIO.output(26, 1)
    GPIO.output(18, 1)
    GPIO.output(24, 0)

    print("Left Backward")

def allStop():
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