from picamera2 import Picamera2, Preview
import time
from datetime import datetime
import RPi.GPIO as GPIO

#pirDataPin=23
pirDataPin=17
ledPin=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirDataPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT)

picam = None

def EnableEventCapture():
	GPIO.add_event_detect(pirDataPin, GPIO.RISING, callback=pirEvent, bouncetime=300)

def DisableEventCapture():
	GPIO.remove_event_detect(pirDataPin)

def CaptureImage():
	filename = "snaps/" + str(datetime.now()) + ".jpg"
	picam.capture_file(filename)
	print(filename)

def pirEvent(channel):
	if GPIO.input(pirDataPin):
		GPIO.output(ledPin, True)
		DisableEventCapture()
		CaptureImage()
		time.sleep(10)
		EnableEventCapture()
		GPIO.output(ledPin, False)

def CloseGracefully():
		picam.stop()
		picam.close()
		GPIO.cleanup()


def Startup():
	global picam

	try:
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

		EnableEventCapture()

		print("ready")
	except:
		CloseGracefully()


Startup()
while True:
	time.sleep(1)

