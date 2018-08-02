import unittest
from unittest.mock import Mock, call
from src.motor import Motor


class TestMotor(unittest.TestCase):
    def setUp(self):
        self.gpio = Mock()
        self.gpio.LOW = 0
        self.gpio.HIGH = 1
        self.sleep = Mock()
        self.FORWARD_PIN = 1
        self.BACKWARD_PIN = 2
        self.motor = Motor(self.gpio, self.sleep, self.FORWARD_PIN, self.BACKWARD_PIN)

    def doTestMotion(self, motion_func, pin):
        delay = 5
        motion_func(delay)
        self.gpio.output.assert_has_calls([call(pin, self.gpio.HIGH),
                                           call(pin, self.gpio.LOW)])
        self.sleep.assert_called_once_with(delay)

    def test_forward_success(self):
        self.doTestMotion(lambda delay: self.motor.forward(delay), self.FORWARD_PIN)

    def test_backward_success(self):
        self.doTestMotion(lambda delay: self.motor.backward(delay), self.BACKWARD_PIN)


if __name__ == '__main__':
    unittest.main()
