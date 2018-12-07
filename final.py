import RPi.GPIO as GPIO
import time
import lcd_lib as lcd
import os

# Pins usados por lcd: 7,8,25,24,23,18

# Pins que quieres usar
input_1=4
input_2=17
output_1=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(input_1, GPIO.IN)
GPIO.setup(input_2, GPIO.IN)
GPIO.setup(output_1, GPIO.OUT)

# Callback para apagado
def my_callback:
	print ("Callback")
	#lcd.adios("Apagando")
	lcd.escribe("Pulsado")
	gpio.output(output_1, True)
	time.sleep(5)
	gpio.output(output_1, 0)

GPIO.add_event_detect(input_1, GPIO.RISING)
GPIO.add_event_callback(input_1, my_callback, bouncetime=3000)


def main():
	lcd.lcd_init()
	lcd.escribe("Ejecucion iniciada",lcd.LCD_LINE_1)


if __name__ == '__main__':
	try:
	  	main()
	except KeyboardInterrupt:
	  	pass
	finally:
		gpio.cleanup()
	 	lcd.adios()
