import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
gpio.setup(27, gpio.OUT)

contador=0
gpio.output(27, 0)
while True:
	if gpio.input(17):
		print "Presencia"+str(contador)
		contador+=1
	time.sleep(1)
gpio.cleanup()
