import os
import logging
import cv2
import time
from cv2 import imshow, waitKey, destroyWindow, imwrite



logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("video_frame_app.log"),
        logging.StreamHandler()
    ]
  )

vid = cv2.VideoCapture(0)



result, image = vid.read()

if result: 
  
    # showing result, it take frame name and image  
    # output 
    imshow("Test", image) 
  
    # saving image in local storage 
    imwrite("Test.png", image) 
  
    # If keyboard interrupt occurs, destroy image  
    # window 
    waitKey(0) 
    destroyWindow("Test") 
  
# If captured image is corrupted, moving to else part 
else: 
    print("No image detected. Please try again") 