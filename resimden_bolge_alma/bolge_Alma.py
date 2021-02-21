import cv2
import numpy as np

resim=cv2.imread("eb.jpg")

kesit=resim[500:1000,200:900]

resim[200:700,200:900]=kesit

resim[500 :150, 300:400, 0]=0
resim[200 :150, 300:400, 1]=0
resim[10 :150, 500:600, 2]=0

#cv2.imshow("resmim: kesit alanı",kesit)
cv2.imshow("resmim:",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()