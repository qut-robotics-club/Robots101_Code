import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory # Import pigpio for jitter free servo control
import time

myGPIO = 21 # GPIO pin for servo PWM control

factory = PiGPIOFactory() # Handle for Socket communicating with pigpio daemon

# Enable Servo Angle Controled
servo = gpiozero.AngularServo(21, min_angle=-90, max_angle=90, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)

# Enable Servo PWM Controled
# servo = Servo(myGPIO, min_pulse_width=minPW, max_pulse_width=maxPW, pin_factory=factory)

# Simple test for opening and closing servo between min & Max gripper states
def OpenCloseTest():
    servo.angle = -45
    time.sleep(2)
    servo.angle = 5
    time.sleep(2)
    servo.angle = -45
    time.sleep(2)
# # Simple test for running gripper smoothly between open and close states using increments
# def StepBetween(Max:int = 0 , Min:int = -45, delay:int = 1):

#     for value in range(Min,Max):
#         value2=(float(value)-10)/10
#         servo.value=value2
#         time.sleep(delay)

#     for value in range(Max-1,-1,-1):
#         value2=(float(value)-10)/10
#         servo.value=value2
#         time.sleep(delay)

# Simple test for running gripper smoothly between open and close states using increments
def StepBetween(Max:int = 0 , Min:int = -45, delay:int = 1):

    for value in range(Min,Max):
        servo.angle = value
        time.sleep(delay)

    for value in range(Max-1,-1,-1):
        servo.angle = value
        time.sleep(delay)


while True:
    OpenCloseTest()
    # StepBetween()