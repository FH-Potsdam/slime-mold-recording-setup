"""
camera controller for tracking slime molds
University of Applied Sciences Potsdam (Germany) @idpotsdam
author: fabiantheblind
license: MIT
"""

import sys # we need this to exit if the GPIO lib is not present
import time # just for testing purpose
import datetime # for timestamps
import os # for path checking

# change these if you like
IMAGEFOLDER = "/home/pi/fhp/images/"
IMAGENAME = "slime"

# leave this alone
TIMESTAMP = 0
# Check if the libraries exist on this system
# if not throw a warning
try:
    import RPi.GPIO as GPIO
    print "GPIO lib is present. Moving on"
except ImportError:
    print "GPIO lib is not installed. Stopping program"
    print "Please install it with the commands:"
    print "$ sudo apt-get update"
    print "$ sudo apt-get install rpi.gpio"
    sys.exit()
try:
    import picamera
    print "picamera lib present moving on"
except ImportError:
    print "picamera lib is not installed. Stopping program"
    print "Please install it with the commands:"
    print "$ sudo apt-get update"
    print "$ sudo apt-get install python-picamera python3-picamera"
    sys.exit()

def lighton(led1, led2, led3, led4):
    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.HIGH)
    GPIO.output(led3, GPIO.HIGH)
    GPIO.output(led4, GPIO.HIGH)


def lightoff(led1, led2, led3, led4):
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(led4, GPIO.LOW)
##
#Add more LEDs as arguments
#
def setup(led1, led2, led3, led4):
    """Setup all that stuff"""
    print "setup GPIO"
    global TIMESTAMP
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.setup(led4, GPIO.OUT)
    if not os.path.exists(IMAGEFOLDER):
        print "folder does not exists. Create it"
        os.makedirs(IMAGEFOLDER)
    ts = time.time()
    TIMESTAMP = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H-%M-%S")



# now run all of that
if __name__ == '__main__':
    try:
        setup(11, 12, 15, 16)
        print "GPIO all set up"
        cam = picamera.PiCamera()
        # this is just for testing
        # the max resolution is
        # 2592 x 1944
        cam.resolution = (640, 480)
        # there cant be a preview when working remote via ssh
        # but if you are in the GUI you can preview the image
        # camera.start_preview()
        # time.sleep(5)
        filename = IMAGEFOLDER + IMAGENAME + TIMESTAMP + ".jpg"
        lighton(11, 12, 15, 16)
        time.sleep(0.2)
        cam.capture(filename)
        time.sleep(0.2)
        lightoff(11, 12, 15, 16)
        print "made a picture and wrote it to ", filename
        cam.close() # close the cam again
        # camera.stop_preview()
        # GPIO.cleanup()
    except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
        print "KeyboardInterrupt"
        GPIO.cleanup() # this ensures a clean exit
    # except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
        # print "Other error or exception occurred!"
    finally:
        print "end. clean up GPIO"
        GPIO.cleanup() # this ensures a clean exit

