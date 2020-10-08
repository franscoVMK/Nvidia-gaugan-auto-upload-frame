from pynput.keyboard import Key, Controller
import win32api, win32con
import pyautogui
import python_imagesearch
from python_imagesearch.imagesearch import imagesearch
import time
import os
from multiprocessing import Pool
from screen_search import *
import autoit



#by Francesco V.M.K

#it upload



Nframe = input("frame number: ")
i = 0
while int(i) < int(Nframe):
    waitTime = 0.3

    search = Search("A.PNG")


    pos = search.imagesearch()

    if pos[0] != -1:
        path = os.path.abspath("./frame/" + str(i) + ".png")
        print(path)
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        time.sleep(0.5)
        autoit.win_wait_active("Apri", 20000)
        time.sleep(0.5)
        autoit.send(path)
        time.sleep(0.5)
        autoit.send("{ENTER}")
        time.sleep(0.5)
        search = Search("B.PNG")
        pos = search.imagesearch()
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
            time.sleep(0.5)
            pyautogui.click(pos[0], pos[1])
            search = Search("C.PNG")
            pos = search.imagesearch()
            if pos[0] != -1:
                print("position : ", pos[0], pos[1])
                time.sleep(0.5)
                pyautogui.click(pos[0], pos[1])
                time.sleep(3)

                search = Search("D.PNG")
                pos = search.imagesearch()
                if pos[0] != -1:
                    print("position : ", pos[0], pos[1])
                    time.sleep(0.5)
                    pyautogui.click(pos[0], pos[1])
                    i = i + 1
                else:
                    print("Convert not found")

            else:
                print("Convert not found")
        else:
            print("Upload not found")
    else:
        print("Browse not found")

