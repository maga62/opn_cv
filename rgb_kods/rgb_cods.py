import cv2
import numpy as np

kartal=cv2.imread("eagle.jpg")

cv2.imshow("kartal",kartal)
print(kartal[(25,10)])

print("resim_boyutu: "+str(kartal.size))
print("resim_ozellik: "+str(kartal.shape))
print("resim_veritipi: "+str(kartal.dtype))
cv2.waitKey(0)
cv2.destroyAllWindows()