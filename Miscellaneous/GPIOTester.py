import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) # Set the GPIO pin naming mode


# Set all GPIO pins to output
for pin in range(2,28):
    GPIO.setup(pin, GPIO.OUT)

for pin in range(2,28):
    GPIO.output(pin, GPIO.LOW)
    
# Iterate over all the pins, print the number, set it to HIGH, wait for user input, set it to LOW
for pin in range(2,28):
    print(pin)
    GPIO.output(pin, GPIO.HIGH)
    input("Press Enter to continue...")
    GPIO.output(pin, GPIO.LOW)