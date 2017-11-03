# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import time
import serial				# may need to do install?
from msvcrt import getch		# read the keyboard!

# forward: 72
# down: 80
# right: 77
# left: 75

cap = cv2.VideoCapture(0)

LEFT=chr(64)
RIGHT=chr(32)
TURRET=chr(16)
NEGATIVE_ON=chr(8)
NEGATIvE_OFF=chr(0)
NEGATIVE_VALUE=chr(0)
COMMAND=chr(0)
NUMBER=chr(0)









# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM9',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)


if (ser.isOpen()):
	ser.close()


ser.open()

while 1:

    key = 0
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    key = cv2.waitKey(1)
   
    if(key == 112):
      
        filename1 = time.strftime("%Y%m%d-%H%M%S")
        filename2 = "images\\" + filename1 + ".jpg"
        cv2.imwrite(filename2 , frame)
        
    if(key)!= -1:

        print key
   
        if (key==113 or key==81):
           break 
        elif (key>2000):
           print "arrow key" #arrow key, get another char
           if (key == 2490368):
               key = 72
           elif (key == 2621440):
               key = 80
           elif (key == 2424832):
               key = 75
           elif (key == 2555904):
               key = 77
    
           ser.write(chr(key))
            # key=ord(getch())
        else:
           continue
        print key
        
 
	
ser.close()
print "all done"
	



