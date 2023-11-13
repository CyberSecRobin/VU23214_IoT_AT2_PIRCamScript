import RPi.GPIO as GPIO​
import time​

inpin=23​

startupWaitTimeInSeconds=2​
motionResetTimeOutInSeconds=1​
mainLoopDelayTimeInSeconds=0.1​

motionActivatedCounter=0​

GPIO.setmode(GPIO.BCM)​
GPIO.setup(inpin, GPIO.IN)​

print("Using GPIO Pin", inpin, "as input for high/low signal.")​
print("Motion timeout reset is", motionResetTimeOutInSeconds, "seconds")​

try: #attempt this code, in a safe (ish) manor​
        time.sleep(startupWaitTimeInSeconds) #Give the sensor time to startup​
        print("Startup complete. Listening for signal on pin", inpin)​\

        while True: #continually loop until cancelled​
                if GPIO.input(inpin): #Pin 23 will be set high (digital 1 or True) when PIR detects motion​
                        motionActivatedCounter+=1​
                        print("Motion detected! (", motionActivatedCounter, ")")​
                        print("Motion cooldown, active in", motionResetTimeOutInSeconds, "second(s)")​
                        time.sleep(motionResetTimeOutInSeconds) #Allow the sensor to reset from true (only if true)​
                        print("Watching......")​
                        print("")​

        time.sleep(mainLoopDelayTimeInSeconds) #give the loop a small delay.  ​

except:​
        print("Exit or Error, performing clean up and exiting")​
        GPIO.cleanup() #If error, clean up and exit​
