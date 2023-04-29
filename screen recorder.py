from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics #height and weight dynamic

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured = cv2.VideoWriter("screen.mp4", fourcc, 20.0, (width, height))

while True:
	img = ImageGrab.grab(bbox=(0,0,width,height))
	img_np=np.array(img)
	img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
	cv2.imshow('Screen Recorder',img_final)
	captured.write(img_final)
	if cv2.waitKey(10) == ord("q"):
		break
	cv2.waitKey(10)
