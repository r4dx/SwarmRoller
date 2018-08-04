import serial


class Sonar:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)

    def read_distance(self):
        def read(obj):
            data = obj.ser.readline().split()
            if len(data) > 0 and data[0] and data[0] != '!!':
                return float(data[0])
            else:
                return None

        res = read(self)
        while res is None:
            res = read(self)

        return res
