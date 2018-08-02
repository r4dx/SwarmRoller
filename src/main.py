from time import sleep
from motor import Motor
import RPi.GPIO as GPIO

FORWARD_PIN = 26
BACKWARD_PIN = 19

GPIO.setmode(GPIO.BCM)

motionMotor = Motor(GPIO, lambda secs: sleep(secs), FORWARD_PIN, BACKWARD_PIN)
motionMotor.forward(1)
sleep(2)
motionMotor.backward(1)
