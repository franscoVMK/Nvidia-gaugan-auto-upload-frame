# Python program to take
# screenshots


import numpy as np
import cv2
import pyautogui

i=0
Nframe = input("Frame Number: ")
while i < int(Nframe):
    # take screenshot using pyautogui
    image = pyautogui.screenshot(region=(50,150, 1000, 700))

    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)

    # writing it to the disk using opencv
    cv2.imwrite("./frame/"+ str(i) + ".png", image)
    i = i +1