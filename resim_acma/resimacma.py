import cv2
import numpy as np

resim=cv2.imread("Lipton.logo.png",)
#resim2=cv2.imread("kus.png")
cv2.imshow("bir lipton logo",resim)
#cv2.imshow("bir lipton logo",resim2)
cv2.imwrite("yeniresim.png",resim) #olan resmi yukardakı 0 vererek grileşdirdik o gri resmi 2 ci resim olarak kayd etddik
print(resim.size)
print(resim.dtype)
print(resim.shape)



cv2.waitKey(0) # pencere acılması
cv2.destroyAllWindows() #pencere carpı basınlınca kapanması 
