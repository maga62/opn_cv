import cv2
import numpy as np


bat=cv2.imread("Batman.jpg")
bat[65:115,250:350,0]=18
bat[65:115,250:350,1]=27
bat[65:115,250:350,2]=15


cv2.imshow("bat fotografı:",bat)




cv2.waitKey()
cv2.destroyAllWindows()