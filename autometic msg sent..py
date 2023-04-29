import pywhatkit
try:
  # pywhatkit.sendwhatmsg("+8801857411320","hi",20,12) 
  pywhatkit.image_to_ascii_art('images.jpg','images.txt')
  print("Successfully Sent!")
except:
	pass