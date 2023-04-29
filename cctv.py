import cv2

cap=cv2.VideoCapture(1)

while cap.isOpened():
	ret,frame1=cap.read()
	ret,frame2=cap.read()
	diff=cv2.absdiff(frame1,frame2)
	gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
	#for sharper and brighter
	blur=cv2.GaussianBlur(gray,(5,5),0)
	_,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
	dilated=cv2.dilate(thresh,None,iterations=3)
	#moving
	contour=cv2.contour
	if(cv2.waitKey(10)==ord('q')):
		break

	cv2.imshow("frame",thresh)