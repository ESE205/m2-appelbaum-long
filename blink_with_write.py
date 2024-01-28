import RPi.GPIO as GPIO
from time import sleep, time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Get user input for LED pin
led_pin = int(input("Enter GPIO pin number for LED: "))
switch_pin = int(input("Enter GPIO pin number for switch: "))

# Set up GPIO pins
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Get the command line argument for the number of blinks
if len(sys.argv) > 1:
    try:
        ITER_COUNT = int(sys.argv[1])
    except ValueError:
        print("Invalid input for number of blinks. Using default value (5).")
        ITER_COUNT = 5
else:
    ITER_COUNT = 5  # Default to 5 blinks if no argument is provided

filename = "data.txt"

try:
    with open(filename, "w") as file:
        start_time = time()
        while ITER_COUNT > 0 and GPIO.input(switch_pin) == GPIO.HIGH:
            elapsed_time = round(time() - start_time, 2)
            switch_state = GPIO.input(switch_pin)
            
            file.write(f"{elapsed_time}\t{switch_state}\n")
            file.flush()  # Ensure data is written immediately to the file
            
            ITER_COUNT -= 1
            GPIO.output(led_pin, GPIO.HIGH)
            sleep(1)
            GPIO.output(led_pin, GPIO.LOW)
            sleep(1)
            print(f"Switch state: {switch_state}")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")

finally:
    GPIO.cleanup()
