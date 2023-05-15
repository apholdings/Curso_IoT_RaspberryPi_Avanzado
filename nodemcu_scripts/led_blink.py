import machine
import time

# Initialize GPIO16 (D0) as an output pin
led = machine.Pin(16, machine.Pin.OUT)

while True:
    led.value(1)  # LED on
    time.sleep(1)  # delay for 1 second
    led.value(0)  # LED off
    time.sleep(1)  # delay for 1 second