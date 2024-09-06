import cv2
import pyautogui
from win32api import getSystemMetrics
import numpy as np
import time

width = getSystemMetrics(0)
height = getSystemMetrics(1)
dim = (width, height)
f = cv2.VdideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", f, 30.0, dim)
now_start_time = time.time()
dur = 10
end_time = now_start_time + dur

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()

    if c_time > end_time:
        break

output.release()
print("---END---")

