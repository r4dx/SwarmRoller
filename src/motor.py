class Motor:
    def __init__(self, gpio, sleep_func, forward_pin, backward_pin):
        self.forwardPin = forward_pin
        self.backwardPin = backward_pin
        self.gpio = gpio
        self.sleepFunc = sleep_func
        gpio.setup(forward_pin, gpio.OUT)
        gpio.setup(backward_pin, gpio.OUT)

    def go(self, pin, delay):
        self.gpio.output(pin, self.gpio.HIGH)
        self.sleepFunc(delay)
        self.gpio.output(pin, self.gpio.LOW)

    def forward(self, delay):
        self.go(self.forwardPin, delay)

    def backward(self, delay):
        self.go(self.backwardPin, delay)