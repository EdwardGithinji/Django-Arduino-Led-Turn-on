import serial
import time

ArduinoSerial=serial.Serial('com7', 9600)
time.sleep(2)

print(ArduinoSerial.readline())
print("Enter 1 to turn LED on and 0 to turn it off")


class Led_onoff:
    def __init__(self, var):
        self.var = var

    def led_on(self):

        self.var == '1'
        return ArduinoSerial.write(self.var.encode())
        #print("LED turned on")
        time.sleep(1)

    def led_off(self):
        self.var == '0'
        return ArduinoSerial.write(self.var.encode())
        #print("LED turned off")
        time.sleep(1)

