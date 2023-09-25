# Install the following modules in the terminal. "pip install numpy", "pip install pyautogui","pip install opencv-python" 
# Importing the required packages
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. we can choose any value and experiment with it.
fps = 60.0

#creating a videowriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# creating and resizing an Empty window to display recording in full time.
# Create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resizing this window
cv2.resizeWindow("Live", 480, 279)

while True:
    #Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    #convert the screenshot to a numpy array
    frame = np.array(img)

    #convert it from BGR to RGB(Blue, Green, Red)to (Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Write it to the output file 
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame) 

    #Stop recording when we press 'q'
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video writer 
out.release()

# Destroy all windows()
cv2.destroyAllWindows()







