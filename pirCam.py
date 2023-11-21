from picamera2 import Picamera2, Preview
import time
from datetime import datetime
import RPi.GPIO as GPIO

pirDataPin=23
ledPin=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirDataPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT)

picam = Picamera2()
config = picam.create_still_configuration(main={"size": (1152, 648)})
picam.configure(config)
picam.start_preview(Preview.NULL)
picam.start()

print("waiting for camera and PIR to warm")
startupLoop = 0
while startupLoop < 10:
	startupLoop = startupLoop + 1
	print(10-startupLoop)
	GPIO.output(ledPin, True)
	time.sleep(0.5)
	GPIO.output(ledPin, False)
	time.sleep(0.5)

print("ready")

while True:
	try:
		if GPIO.input(pirDataPin):
			filename = str(datetime.now()) + ".jpg"
			print("snap " + filename)
			picam.capture_file("snaps/" + filename)
			GPIO.output(ledPin, True)
			time.sleep(10)
			GPIO.output(ledPin, False)
		else:
			GPIO.output(ledPin, False)
			#print("all quiet.  waiting")
			time.sleep(0.5)
	except:
		picam.stop()
		picam.close()
		GPIO.cleanup()
