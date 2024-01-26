import RPi.GPIO as GPIO
from time import sleep
import argparse

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def blink_led(pin, iterations):
    for _ in range(iterations):
        GPIO.output(pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(pin, GPIO.LOW)
        sleep(1)

def main():
    parser = argparse.ArgumentParser(description='Blink an LED on Raspberry Pi for a specified number of times.')
    parser.add_argument('-n', '--iterations', type=int, default=5, help='Number of times to blink the LED')
    parser.add_argument('-p', '--pin', type=int, default=11, help='GPIO pin number')
    args = parser.parse_args()

    pin = args.pin
    iterations = args.iterations

    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    try:
        blink_led(pin, iterations)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
