import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
#gpio.setup(27, gpio.OUT)

prev_input = 0
while True:
  input = gpio.input(17)
  if ((not prev_input) and input):
    print("Button pressed")
  prev_input = input
  time.sleep(0.05)
gpio.cleanup()
