# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import time
import serial				       # may need to do install?
import serial.tools.list_ports # get open com port
from msvcrt import getch		# read the keyboard!

# forward: 72
# down: 80
# right: 77
# left: 75

#opens serial port
def openSerial():
    openPorts = serial.tools.list_ports.comports()    
    print(openPorts)
    if not openPorts:
        print("No open ports")
        exit()
        
    ser = serial.Serial(
        openPorts[0].device,
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    if (ser.isOpen()):
        ser.close()
    ser.open()
    return ser

#open video camera
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.avi',-1, 20, (frame_width,frame_height),False)


LEFT=chr(64)
RIGHT=chr(32)
TURRET=chr(16)
NEGATIVE_ON=chr(8)
NEGATIvE_OFF=chr(0)
NEGATIVE_VALUE=chr(0)
COMMAND=chr(0)
NUMBER=chr(0)

ker3 = np.ones((3,3))/9.0
ker5 = np.ones((5,5))/25.0
ker9 = np.ones((9,9))/81.0

ser = openSerial()

#display video, do user inputs
while 1:
    key = 0
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray9 = cv2.filter2D(gray,-1,ker3)
    #gray25 = cv2.filter2D(gray,-1,ker5)
    #gray81= cv2.filter2D(gray,-1,ker9)
    
    canny = cv2.Canny(gray9, 100,200)
    #canny3 = cv2.Canny(gray9, 50,200) #works well
    #canny5 = cv2.Canny(gray9, 100,250)
    #canny9 = cv2.Canny(gray9, 50,250)

    # Display the resulting frame
    cv2.imshow('frame',canny)
    out.write(canny)
    #cv2.imshow('gray9',canny3)
    #cv2.imshow('gray25',canny5)
    #cv2.imshow('gray81',canny9)
    key = cv2.waitKey(1)
   
    if(key == 112):
      
        filename1 = time.strftime("%Y%m%d-%H%M%S")
        filename2 = "images\\" + filename1 + ".jpg"
        cv2.imwrite(filename2 , frame)
        
    if(key)!= -1:

        print key
   
        if (key==113 or key==81): #user quits
           break 
        elif (key==115 or key == 83):
            key = 83
            ser.write(chr(key))
        elif (key>2000):
           print "arrow key"      #arrow key, send correct signal
           if (key == 2490368):   #forward
               key = 72
           elif (key == 2621440): #back
               key = 80
           elif (key == 2424832): #left
               key = 75
           elif (key == 2555904): #right
               key = 77
           ser.write(chr(key))
        else:
           continue
        
        print key
        
ser.close()
out.release()
print "all done"
	

    


