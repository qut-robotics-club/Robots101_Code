import RPi.GPIO as GPIO
import time

# Set Boards & Motors Up
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # 1A
GPIO.setup(26, GPIO.OUT) # 1B
GPIO.setup(16, GPIO.OUT) # 2A
GPIO.setup(19, GPIO.OUT) # 2B

# Create PWM Object
A1 = GPIO.PWM(20,100)
A2 = GPIO.PWM(16,100)
B1 = GPIO.PWM(26,100)
B2 = GPIO.PWM(19,100)

A1.start(0)
A2.start(0)
B1.start(0)
B2.start(0)

# Move Forward
# Set the first two pins to move forward at x speed
print("Move forward at 50%")
B1.ChangeDutyCycle(0)
B2.ChangeDutyCycle(50)
A1.ChangeDutyCycle(50)
A2.ChangeDutyCycle(0)
time.sleep(5)

print("Move backwards at 50%")
B1.ChangeDutyCycle(50)
B2.ChangeDutyCycle(0)
A1.ChangeDutyCycle(0)
A2.ChangeDutyCycle(50)
time.sleep(5)

print("Turn left at 50%")
B1.ChangeDutyCycle(0)
B2.ChangeDutyCycle(0)
A1.ChangeDutyCycle(50)
A2.ChangeDutyCycle(50)
time.sleep(5)

print("Turn right at 50%")
B1.ChangeDutyCycle(50)
B2.ChangeDutyCycle(50)
A1.ChangeDutyCycle(0)
A2.ChangeDutyCycle(0)
time.sleep(5)

print("Stopping")
B1.ChangeDutyCycle(0)
B2.ChangeDutyCycle(0)
A1.ChangeDutyCycle(0)
A2.ChangeDutyCycle(0)
B1.stop()
B2.stop()
A1.stop()
A2.stop()
time.sleep(5)

GPIO.cleanup()
print("Everythin's cleaned up")