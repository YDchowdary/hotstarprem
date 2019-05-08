
import PIL.ImageGrab
import pyautogui
import time


"""
while()
	check black
	if black
		keys
	else 
		exit()
""""

while 1:
	#check black
	
	
	if PIL.ImageGrab.grab().load()[700,350]=='#000fff000':
		pyautogui.keyDown("shift")

        	pyautogui.keyDown("ctrl")
   		pyautogui.press("r")
		pyautogui.keyUp("shift")

        	pyautogui.keyUp("ctrl")
		time.sleep(5)
	else
		break
