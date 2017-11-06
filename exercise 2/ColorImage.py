import cv2
img = cv2.imread("baboon.jpg")
blue,green,red=cv2.split(img)
hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
Ycrbr=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
y,cr,br=cv2.split(Ycrbr)
hue,saturation,value=cv2.split(hsv)
#cv2.imshow ('Blue.jpg',hsv[:,:,0])
#cv2.imshow ('Green',hsv[:,:,1])
#cv2.imshow ('Red', hsv[:,:,2])

cv2.imwrite("Hue.jpg", hue)
cv2.imwrite ("Saturation.jpg",saturation)
cv2.imwrite("Value.jpg", value)

cv2.imwrite("Y.jpg", y)
cv2.imwrite ("Cr.jpg",cr)
cv2.imwrite("Br.jpg", br)

cv2.imwrite("blue.jpg", blue)
cv2.imwrite ("green.jpg",green)
cv2.imwrite("red.jpg", red)
cv2.waitKey(0) 
cv2.destroyAllWindows()

#brightYCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)