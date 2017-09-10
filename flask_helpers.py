import tinder_api as tinder
import cv2
import numpy as np
import urllib

def matches():
    if tinder.authverif() == True: 
       matches = tinder.get_recommendations()
       return matches
    else: 
        print('Sorry, something went wrong')
        return None

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image



