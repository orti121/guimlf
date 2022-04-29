import serial
from serial import Serial
import time


class SerialControl:

    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = None

    def open_serial(self):
        try:
            self.serial = Serial(self.port, 115200, timeout=1, write_timeout=0.1)
            print("The port is available")
            serial_port = "Open"
            time.sleep(2)
        except serial.serialutil.SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close_serial(self):
        time.sleep(0.2)
        self.serial.close()

    def write_servo(self, id, ang):
        angledata = ang
        if id == 1:
            angledata = 2 * angledata
        self.serial.write(('&' + str(id) + ':' + str(angledata)).encode())

    def read_status(self):
        ser_status = self.serial.isOpen()
        print(f"Serial Open: {ser_status}")
        if ser_status:
            status = "Working Clean"
            print(f"status: {status}")

    def read_sensors(self):
        status = "Not implemented"
        print(f"Sensor status: {status}")

    def run_effector(self):
        status = "Not implemented"
        print(f"Effector status: {status}")
