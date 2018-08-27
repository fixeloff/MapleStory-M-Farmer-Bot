from pyautogui import locateCenterOnScreen, locateOnScreen, click, mouseDown, mouseUp
import random
import threading
import time
import sys
import datetime

screenDimension = [2560, 1440]
screenScalingFactor = 1
#screenDimension = [2880, 1800]
#screenScalingFactor = 2

questStart = [480, 540]
imagesToggle = 'questClaim.png'

started = 0
images = ['questScroll.png', 'questClaim.png', 'questComplete.png', 'questSkip.png', 'questAccept.png', 'questComplete.png', 'questAvailable.png', 'questMultiComplete.png']
searchX = dict(shadow='andy')
searchY = dict(shadow='andy')
searchM = [240, 240]

def questBot():
	global started, searchX, searchY
	if started:
		coord = [0,0]
		for x in range(1,len(images)):
			found = 0
			try:
				if images[x] in searchX:
					if locateCenterOnScreen(images[x], grayscale=True, region=(int(searchX[images[x]]),int(searchY[images[x]]),searchM[0],searchM[1])) is not None:
						(coord[0], coord[1]) = locateCenterOnScreen(images[x], grayscale=True, region=(int(searchX[images[x]]),int(searchY[images[x]]),searchM[0],searchM[1]))
						found = not found
				else:
					if locateCenterOnScreen(images[x], grayscale=True) is not None:
						(coord[0], coord[1]) = locateCenterOnScreen(images[x], grayscale=True)
						searchX[images[x]] = str(coord[0] - searchM[0]/2)
						searchY[images[x]] = str(coord[1] - searchM[1]/2)
						found = not found
				if found:
					mouseClick(coord[0]/screenScalingFactor, coord[1]/screenScalingFactor)
					print("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - Clicked '" + images[x] + "'")
					if images[x] == imagesToggle:
							started = not started
					found = not found
			except IOError as e:
				print("Catching IO Error from pyautogui")
	else:
		mouseClick(questStart[0], questStart[1])
		print("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m %H:%M:%S') + "] - Clicked 'Start Quest'")
		started = not started

def mouseClick(xi,yi):
	mouseDown(x=xi, y=yi)
	time.sleep(random.uniform(0.4,0.7))
	mouseUp()