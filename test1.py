import sys

sys.path.append('/home/pi/mlf/core')
#from serial_control import SerialControl
from mk2robot import MK2Robot
# from core.serial_control import SerialControl #for pc
# from core.mk2robot import MK2Robot #for pc
import time

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
#robot_serial = SerialControl()
# robot_serial = SerialControl("COM5") #for pc
#robot_serial.open_serial()

def sendxyz():
    try:
        Xval = int(input("X: "))
        Yval = int(input("Y: "))
        Zval = int(input("Z: "))
        q0, q1, q2 = robot.inverse_kinematics(Xval, Yval, Zval)
        #robot_serial.write_servo(1, 45 + q0)
        #robot_serial.write_servo(2, 90 - q1)
        #robot_serial.write_servo(3, q2 + q1)
        print(f"q0 = {q0}")
        print(f"q1 = {90-q1}")
        print(f"q2 = {q1+q2}")
        time.sleep(0.4)
    except:
        print("ingrese un valor válido")
        pass

def sendang():
    q0val = int(input("q0: "))
    q1val = int(input("q1: "))
    q2val = int(input("q2: "))
    #robot_serial.write_servo(1, q0val)
    #robot_serial.write_servo(2, q1val)
    #robot_serial.write_servo(3, q2val)
    print(f"q0 = {q0val}")
    print(f"q1 = {90-q1val}")
    print(f"q2 = {q1val+q2val}")
    time.sleep(0.4)

def sendhome():
    #robot_serial.write_servo(1, 45)
    #robot_serial.write_servo(2, 90)
    #robot_serial.write_servo(3, 90)
    print("sending home")
    pass

sendxyz()
sendang()
sendhome()