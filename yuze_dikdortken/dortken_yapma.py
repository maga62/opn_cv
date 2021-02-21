import cv2


rsm=cv2.imread("aa.jpg")

cv2.rectangle(rsm,(250,100),(325,225),[0,255,0],4)
cv2.imshow("hababam:",rsm)




cv2.waitKey(0)
cv2.destroyAllWindows()