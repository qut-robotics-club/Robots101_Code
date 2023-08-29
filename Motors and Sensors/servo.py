import RPi.GPIO as GPIO
import time

# Set Board Up
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

# Create PWM Object
servo = GPIO.PWM(12,50)

# Initialise servo
servo.start(0)					# start(0) means start at PWM Duty Cycle of 0 (0-100%)
print("Waiting for 1 second")
time.sleep(1)

# SG90 Servo Data Info
# - Pulse Cycle - 20ms
# - PWM Range - 500us to 2400us
#    - Position -90: 500us		(500/20000 * 100 =  2.5%)
# 	 - Position   0: 1450us    (1450/20000 * 100 = 7.25%)
#    - Position  90: 2400us    (2400/20000 * 100 =   12%)
# 
# Note you can convert a desired angle into a DC using the following formula
# DC = DC_Range*((angle - min_angle)/(angle_range)) + DC_Min

print("Rotate at a interval of 36 degrees")
duty = 2.5
while duty <= 12:
    servo.ChangeDutyCycle(duty)
    time.sleep(3)
    duty = duty + 1.9;

while duty >= 2.5:
    servo.ChangeDutyCycle(duty)
    time.sleep(2)
    duty = duty - 1.9;

print("Going to duty cycle 90")
servo.ChangeDutyCycle(12)
time.sleep(5)

print("Going to duty cycle 0")
servo.ChangeDutyCycle(7.25)
time.sleep(5)

print("Going to duty cycle 90")
servo.ChangeDutyCycle(12)
time.sleep(5)

print("Going to duty cycle -90")
servo.ChangeDutyCycle(2.5)
time.sleep(5)

print("Shutting down")
servo.ChangeDutyCycle(0)
time.sleep(5)

servo.stop()
GPIO.cleanup()
print("Everythin's cleaned up")