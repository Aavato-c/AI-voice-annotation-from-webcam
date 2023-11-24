import os
import logging
import cv2
import time


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