import cv2
import numpy as np

resim=cv2.imread("eagle.jpg")

resim[50,30]=[255,255,255]
resim[50,31]=[255,255,255]
resim[50,32]=[255,255,255]
resim[50,33]=[255,255,255]
resim[50,34]=[255,255,255]
resim[50,35]=[255,255,255]
resim[50,36]=[255,255,255]
resim[50,37]=[255,255,255]
resim[50,38]=[255,255,255]
resim[50,39]=[255,255,255]

#for l in range(100):
   # resim[250,l]=[255,255,255]
#yukardakı işlemi tek forla düz çizgi çektirme

#for i in range(200):
    #resim[55,i]=[255,255,255]
    #for j in range(100):
        #resim[300,j]=[255,255,255] 

for i in range(200):
    resim[55,i]=[255,255,255]
    for j in range(100):
        resim[300,j]=[255,255,255]
    
    
cv2.imshow("kartal:",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()