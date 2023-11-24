import os
import logging
import cv2
import time
from cv2 import imshow, waitKey, destroyWindow, imwrite
import datetime



logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("video_frame_app.log"),
        logging.StreamHandler()
    ]
  )



def getFrame():
    vid = cv2.VideoCapture(0)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    hasFrames, image = vid.read()
    if hasFrames:
        imshow("Current_image", image) 
        imwrite("./media/CURRENT.jpg", image,)
        imwrite(f"./media/archive/IMG_{timestamp}.jpg", image,)
        destroyWindow("Current_image") 
        logger.debug("Image saved")
    else:
        logger.info("Couldn't get image. We'll wait a sec and try again")
        time.sleep(3)
        vid.release()
        getFrame()

    return image



if __name__ == "__main__":
    debug_max_loop = 50
    while True:
        getFrame()
        time.sleep(3)
        debug_max_loop -= 1
        if debug_max_loop == 0:
            break


