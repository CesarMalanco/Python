# Author: reDragonCoder

# Libraries
import pyautogui
import cv2
import numpy as np

# Resolution
resolution=(1920, 1080)

# Video codec
codec=cv2.VideoWriter_fourcc(*'XVID')

# Output file
filename="Recording.avi"

# Frame rate
fps=60.0

# VideoWriter object
out=cv2.VideoWriter(filename, codec, fps, resolution)

# Display the recording in real-time
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

# Videorecording
while True:
    # Take screenshot
    img=pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame=np.array(img)

    # Convert it from BGR to RGB
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Display the recordig screen
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1)==ord('q'):
        break

# Release the videwriter
out.release()

# Detroy all windows
cv2.destroyAllWindows()
