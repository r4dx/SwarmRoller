import time


class Sonar:
    def __init__(self, gpio, sleep_func, trigger_pin, echo_pin):
        self.gpio = gpio
        self.triggerPin = trigger_pin
        self.echoPin = echo_pin
        self.sleep_func = sleep_func
        self.uInS = 1000000.0
        gpio.setup(trigger_pin, gpio.OUT)
        gpio.setup(echo_pin, gpio.IN)

    def _udelay(self, microseconds):
        self.sleep_func(microseconds / self.uInS)

    def _clear_trigger_pin(self):
        self.gpio.output(self.triggerPin, self.gpio.LOW)
        self._udelay(2)

    def _pulse_in(self):
        start = time.time()
        tries = 10
        while self.gpio.input(self.echoPin) != self.gpio.HIGH and tries > 0:
            tries -= 1

        if tries <= 0:
            raise Exception("Never returned")

        return (time.time() - start) * self.uInS

    def obstacle_distance_cm(self):
        self._clear_trigger_pin()
        self.gpio.output(self.triggerPin, self.gpio.HIGH)
        # find in specs and name properly
        self._udelay(10)
        self.gpio.output(self.triggerPin, self.gpio.LOW)
        durationUs = self._pulse_in()

        SPEED_OF_SOUND_CM_uS = 0.034
        return durationUs * SPEED_OF_SOUND_CM_uS / 2