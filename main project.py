from tkinter import *
import cv2
import datetime
import sounddevice
from scipy.io.wavfile import write
from PIL import ImageGrab
import numpy as np
import cv2
from ffpyplayer.player import MediaPlayer
from win32api import GetSystemMetrics #height and weight dynamic
root=Tk()
def video():
	cap=cv2.VideoCapture(0)#0 thakte camera on 
	# cap.set(3,700)
	# cap.set(4,100)
	fourcc=cv2.VideoWriter_fourcc(*'mp4v')
	out=cv2.VideoWriter("abc.mp4",fourcc,20.0,(640,480))
	while cap.isOpened(): #cap.isOpened()=video thikthak hole while loop e jabe
		ret,frame=cap.read()
		if ret==True:
			out.write(frame)
			font=cv2.FONT_HERSHEY_SIMPLEX
			#text="Height "+str(cap.get(4))+" Width "+str(cap.get(3))
			dat=str(datetime.datetime.now())
			cv2.putText(frame,dat,(10,30),font,1,(0,255,255),2,cv2.LINE_AA)
			#gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			cv2.imshow("frame",frame)
			if(cv2.waitKey(1) & 0xFF == ord('q')):
				break
		else:
			break
	cap.release()
	cv2.destroyAllWindows()
def voice():
	fps=44100
	duration=int(input("Duration time ?"))
	print("recording....")
	record=sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
	sounddevice.wait()
	print("done")
	write("output.wav",fps,record)
def screen():
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
def play():
	video_path="screen-capture.webm"
	video=cv2.VideoCapture(video_path)
	player = MediaPlayer(video_path)
	while True:
	    grabbed, frame=video.read()
	    audio_frame, val = player.get_frame()
	    if not grabbed:
	        print("End of video")
	        break
	    if cv2.waitKey(28) & 0xFF == ord("q"):
	        break
	    cv2.imshow("Video", frame)
	    if val != 'eof' and audio_frame is not None:
	        #audio
	        img, t = audio_frame 
	video.release()
	cv2.destroyAllWindows()
label=Label(root,text="Video Audio app").pack()
button_video=Button(root,text="Video Recorder",command=video)
img = PhotoImage(file="video.gif") # make sure to add "/" not "\"
button_video.config(image=img)
button_video.pack()
button_screen=Button(root,text="Screen Recorder",command=screen).pack()
button_voice=Button(root,text="Voice recorder",command=voice).pack()
button_play=Button(root,text="Play Audio with Video",command=play).pack()
root.mainloop()