#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time

servo = 21


#define MIN_WIDTH 1000
#define MAX_WIDTH 2000


pulseWidth = 1000
increment = 100

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency( servo, 50 )

def OpenCloseTest():

    pwm.set_PWM_frequency( servo, 5 )

    print( "0 deg" )
    print(0)
    pwm.set_servo_pulsewidth( servo, 1000  ) ;
    time.sleep( 3 )

    print( "15 deg" )
    print(500)
    pwm.set_servo_pulsewidth( servo, 2000 ) ;
    time.sleep( 3 )

def setInterval():
    pwm.set_servo_pulsewidth(pulseWidth);

    pulseWidth += increment
    if (pulseWidth >= 2000): 
        increment = -100
    if (pulseWidth <= 1000): 
        increment = 100 
    
while True:
    OpenCloseTest()
    # setInterval()
    