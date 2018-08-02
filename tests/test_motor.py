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

    def test_forward_success(self):
        delay = 5
        self.motor.forward(delay)
        self.gpio.output.assert_has_calls([call(self.FORWARD_PIN, self.gpio.HIGH),
                                           call(self.FORWARD_PIN, self.gpio.LOW)])
        self.sleep.assert_called_once_with(delay)


if __name__ == '__main__':
    unittest.main()
