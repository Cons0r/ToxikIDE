import replit.audio
import platform
import os
import tkinter

def run():
	replit.audio.play_file('sound.mp3', 1, False, 0, 'jalert')
def allowedOS():
	if platform.system() == 'Windows':
		return True
	else:
		return False
def getOS():
	return platform.system()
def inject():
	os.rename('main.py','main2.py')
	os.rename('inject.py','main.py')