import serial


class Sonar:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)

    def read_distance(self):
        data = self.ser.readline()
        float(data)
