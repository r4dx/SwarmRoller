from time import sleep
import RPi.GPIO as GPIO

PIN_NUM = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM, GPIO.OUT)
GPIO.output(PIN_NUM, GPIO.HIGH)
sleep(5)
GPIO.output(PIN_NUM, GPIO.LOW)