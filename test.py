import time
import RPi.GPIO as GPIO

p=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(p, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
#GPIO.setup(8, GPIO.IN)
#GPIO.setup(9, GPIO.IN)
#GPIO.setup(12, GPIO.IN)

while True:
	if GPIO.input(p):
		print("High")
		GPIO.output(24, True)
	else:
		print("Low")
		GPIO.output(24, False)

#	print(GPIO.input(p))
#	print(GPIO.input(2))
#	print(GPIO.input(8))
#	print(GPIO.input(9))
#	print(GPIO.input(12))

	time.sleep(1)
