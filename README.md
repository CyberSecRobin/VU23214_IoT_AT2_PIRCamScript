# VU23214_IoT_AT2_PIRCamScript
Code to use a PIR motion sensor and pi-cam with Raspberry pi (pi4) to save snapshots of motion events.

## test.py ##
[test.py](https://github.com/CyberSecRobin/VU23214_IoT_AT2_PIRCamScript/blob/main/test.py) is simply to do some low level GPIO/Pin testing in case of issues.  Particularly useful to check you are using the correct pins.

## pirCam.py ##
[piCam.py](https://github.com/CyberSecRobin/VU23214_IoT_AT2_PIRCamScript/blob/main/pirCam.py) is a primitive script which simply loops over and over again; not the best method but works as a short, sharp, easily typed to use the device rather than look at good code practice.

## pirEvent.py ##
[piEvent.py](https://github.com/CyberSecRobin/VU23214_IoT_AT2_PIRCamScript/blob/main/pirEvent.py) is an improved version with better code structure and utilising event listeners and exception handling. This is the reccommended version.
