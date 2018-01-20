import cv2
import numpy as np
 
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
# Using DIVX codec, 20fps, 720p, False flag specifies grayscale video 
# The flag must be set correctly or video will not output correctly
out = cv2.VideoWriter('output.avi',1, 20, (frame_width,frame_height),False)
 
while(True):
  ret, frame = cap.read()                          # Read a frame
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # Convert to grayscale
  edge = cv2.Canny(gray, 50, 150)                  # Canny edge detection
  
  # Display the resulting frame    
  cv2.imshow('frame',edge)
  # Write the frame into the file 'output.avi'
  out.write(edge)
 
  # Press Q on keyboard to stop recording
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 
