from pyautogui import *
import pyautogui
import pyautogui as pag
import random
import time
import keyboard
import numpy as np
import win32api, win32con

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(2)

while keyboard.is_pressed('q') == False:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(np.random.uniform(3,10))
    click()
    time.sleep(np.random.uniform(0.1,1))
    pyautogui.keyDown('space')
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp('space')
    pyautogui.keyDown('w')
    time.sleep(0.01)
    pyautogui.keyUp('w')
    time.sleep(2)
    pyautogui.keyDown('s')
    time.sleep(0.01)
    pyautogui.keyUp('s')
