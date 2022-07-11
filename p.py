import pyautogui
import time
import playsound
time.sleep(2)
# take a screenshot of the screen 
while True:
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel((1586, 1029))
    if color == (205, 0, 0):
        playsound.playsound('beep.mp3')
