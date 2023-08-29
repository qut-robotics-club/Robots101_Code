from mobility import *
import time
if __name__ == "__main__":

    # Initialise motors
    MotorA = Motor(19,16)
    MotorB = Motor(26,20)

    # Each motor can be controlled individually like so:
    MotorA.forward(100)
    time.sleep(1)
    MotorA.stop()
    time.sleep(1)
    MotorA.backward(100)
    time.sleep(1)
    MotorA.stop()

    # Or you can control both motors at the same time using the static methods:
    Motor.moveForward(100)
    time.sleep(1)
    Motor.moveReverse(100)
    time.sleep(1)
    Motor.stopAll()
    Motor.rotate(100)
    time.sleep(1)
    Motor.rotate(-100)
    time.sleep(1)
    Motor.stopAll()
    
    # Alternatively (and preferrably) use the Motor.move(linear, angular) command to move fluently. This is not a perfect implementation since there is
    # no closed loop, but it is a nice guesstimate

    Motor.move(100, 0)
    time.sleep(1)
    Motor.move(50, 20)
    time.sleep(1)
    Motor.move(50, -20)
    time.sleep(1)
    Motor.move(0, 50)
    time.sleep(1)
    Motor.move(0, -50)
    time.sleep(1)
    Motor.stopAll()


    # The library also does the cleanup at the end of execution. So even while running, if the program ends
    # Motors *Should* stop automatically.
    # However, if you want to nicely clean up after yourself, the Motor.cleanup() method will make sure everything is nice and tidy when you're done

    Motor.cleanup()
