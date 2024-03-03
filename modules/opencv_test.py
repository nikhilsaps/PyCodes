# Importing the OpenCV library 
import cv2 
# Reading the image using imread() function 
image = cv2.imread('image.png') 

# Extracting the height and width of an image 


cv2.resize(image,(100,100))
h, w = image.shape[:2] 
# Displaying the height and width 
print(f"Height = {h}, Width = {w}") 
