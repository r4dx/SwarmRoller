from time import sleep
from motor import Motor
from sonar import Sonar
import RPi.GPIO as GPIO


def test_motor():
    FORWARD_PIN = 26
    BACKWARD_PIN = 19

    motionMotor = Motor(GPIO, lambda secs: sleep(secs), FORWARD_PIN, BACKWARD_PIN)
    motionMotor.forward(1)
    sleep(2)
    motionMotor.backward(1)


def test_sonar():
    sonar = Sonar()
    while True:
        distance = sonar.get_distance()
        print(distance)


GPIO.setmode(GPIO.BCM)
test_sonar()