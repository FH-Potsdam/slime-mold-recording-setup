#!/usr/bin/env python
"""
control an arduino from your raspberry pi over serial
"""

import sys # we need this to exit if the GPIO lib is not present
import time # for timing
try:
    import serial
    print "GPIO pySerial is present. Moving on"
except ImportError:
    print "GPIO lib is not installed. Stopping program"
    print "Please install it with the commands:"
    print "$ sudo apt-get update && sudo apt-get upgrade"
    print "$ sudo apt-get install python3-pip python-pip"
    print "$ sudo pip install pyserial"
    sys.exit()



# # now run all of that
if __name__ == '__main__':
    try:
        ser = serial.Serial("/dev/ttyACM0", 9600)
        while True:
            ser.write('0')
            print "LED 13 is on"
            time.sleep(1)
            ser.write('1')
            print "LED 13 is off"
            time.sleep(1)

    except KeyboardInterrupt:
        print "\nbye bye"
    finally:
        print "\nbye bye"
