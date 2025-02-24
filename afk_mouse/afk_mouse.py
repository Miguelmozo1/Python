# terminal -> python3 -m pip install pyautogui

import pyautogui as pag
import random
import time


# should track so in case mouse is moved, it breaks the while loop, if it hasn't been moved in a specified time, to continue loop
    # /\ not implemented yet



while True:
    curr_mouse_coor = pag.position()
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(3)
    print("running")