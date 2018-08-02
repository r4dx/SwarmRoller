from time import sleep
import src.motor.Motor as Motor
import RPi.GPIO as GPIO

FORWARD_PIN = 26
BACKWARD_PIN = 19
motionMotor = Motor(GPIO, lambda secs: sleep(secs), FORWARD_PIN, BACKWARD_PIN)
motionMotor.forward(1)
sleep(2)
motionMotor.backward(1)