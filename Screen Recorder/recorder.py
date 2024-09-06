import cv2
import pyautogui
from win32api import getSystemMetrics
import numpy as np
import time

width = getSystemMetrics(0)
height = getSystemMetrics(1)

dim = (width, height)

f = cv2.VdideoWriterfourcc(*"XVID")

output = cv2.VideoWriter("test.mp4", f, 30.0, dim)

nowstarttime = time.time()
dur = 10
endtime = nowstarttime + dur

while True:
    image = pyautogui.screenshot()