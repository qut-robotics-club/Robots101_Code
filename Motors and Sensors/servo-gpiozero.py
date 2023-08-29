import gpiozero
import time

servo = gpiozero.AngularServo(21, min_pulse_width=0.0006, max_pulse_width=0.0023)

while True:
    servo.angle = 90
    time.sleep(2)
    servo.angle = 0
    time.sleep(2)
    servo.angle = -90
    time.sleep(2)
    
