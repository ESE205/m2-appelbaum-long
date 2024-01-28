import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1 = int(input("Enter GPIO pin number: "))  # Get pin number from user
ITER_COUNT = int(input("Enter iteration count: "))  # Get iteration count from user

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)

while ITER_COUNT > 0:
    ITER_COUNT -= 1
    GPIO.output(pin1, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin1, GPIO.LOW)
    sleep(1)

GPIO.cleanup()
