# Description: Gripper class for controlling the gripper servo
import os
import subprocess
import time
try:
    import pigpio
except ImportError:
    print("pigpio not found, please install pigpio and try again 'pip install pigpio'")
    exit()

class Gripper:
    import os

    def __init__(self, servoPin, openDC=1600, closeDC=1000):
        self.servoPin = servoPin
        self.openDC = openDC
        self.closeDC = closeDC
        self.scalingFactor = 45 / (self.openDC - self.closeDC)

            
        self.gpio = pigpio.pi()
        
        
        try:
            self.gpio.set_mode(self.servoPin, pigpio.OUTPUT)
        except:
            print("Error setting servo pin mode. Attempting to start daemon.")
            
            subprocess.run(["sudo", "pigpiod"])
            self.gpio.set_mode(self.servoPin, pigpio.OUTPUT)
            print("Process start successfully.")
            
                
        self.gpio.set_PWM_frequency( self.servoPin, 50 )
        self.gpio.set_servo_pulsewidth( self.servoPin, self.openDC )
        
    def open(self):
        self.gpio.set_servo_pulsewidth( self.servoPin, self.openDC )
        
    def close(self):
        self.gpio.set_servo_pulsewidth( self.servoPin, self.closeDC )
        
    @property
    def pulseWidth(self):
        return self.gpio.get_servo_pulsewidth(self.servoPin)
    
    @pulseWidth.setter
    def pulseWidth(self, pulseWidth):
        self.gpio.set_servo_pulsewidth(self.servoPin, pulseWidth)
    
    @property
    def angle(self):
        return (self.gpio.get_servo_pulsewidth(self.servoPin) - self.closeDC) * self.scalingFactor
    
    @angle.setter
    def angle(self, angle):
        self.gpio.set_servo_pulsewidth(self.servoPin, (angle / self.scalingFactor) + self.closeDC)
        
        
###############################################  
##                                           ##
##         Instructions for use:             ##
##                                           ##
##                                           ##
###############################################

# Test code
if __name__ == "__main__":
    # Import the library
    # from gripper import Gripper
    # Import the gripper object, using the pin
    gripper = Gripper(21)
    
    # To open the gripper, call the open function
    gripper.open()
    
    # To close the gripper, call the close function
    gripper.close()
    
    # You can get the pulsewidth of the gripper by doing this:
    print(gripper.pulseWidth)
    
    # You can also set the pulsewidth of the gripper by doing this:
    gripper.pulseWidth = 1000
    
    # You can also manually set the angle by doing this:
    gripper.angle = 0
    
    # You can also get the angle by doing this:
    print(gripper.angle)
    
    # Some testing code
    while True:
        gripper.open()
        print(gripper.angle)
        time.sleep(2)
        gripper.close()
        print(gripper.angle)
        time.sleep(2)