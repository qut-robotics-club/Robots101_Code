import RPi.GPIO as GPIO
import time
import mobility as mob
import sensor as sens

close = 4 # cm
far = 15 # cm
max_dut = 75

Gradient = max_dut/(15-4)

def map(distance):
    if distance > far:
        return 0
    elif distance < close:
        return max_dut
    else:
        duty = (distance - close)*Gradient
        return duty

period = 0.1

if __name__ == '__main__':
    try:
        mob.init()
        sens.init()

        MotorA = mob.Motor(26,20)
        MotorB = mob.Motor(16,19)

        while True:
            start = time.time()
            dist = sens.distance()
            
            # Map distance to PWM value
            vel = map(dist)
            MotorA.backward(vel)
            MotorB.backward(vel)

            print ("Measured Distance = %.1f cm" % dist)
            print ("Output Duty Cycle = %.1f " % vel)
            end = time.time()
            left = end - start
            if (left >= period):
                print("Frequency is too high")
            else:
                sleep_time = period - left
                time.sleep(period)
 
        # Reset by pressing CTRL + C

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        mob.Motor.cleanup()
        sens.clear()
