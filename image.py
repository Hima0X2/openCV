import cv2
img= cv2.imread('images.jfif',1)#pic read krar jnno
#print(img)
cv2.imshow('image',img) #iamshow(title,pic)
#cv2.waitKey(5000) #5 sec show this pic,0 dile cross na kora porjonto thakbe
k= cv2.waitKey(0)
if k==27: #esc key
	cv2.destroyAllWindows()
elif k==ord('s'): #s key press
	cv2.imwrite('images.jpg',img)