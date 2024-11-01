import cv2
import numpy as np
import main

#PREPROCESSING:-
img=cv2.imread("omr.jpg")
img=cv2.resize(img,(500,500))
imgContours=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny=cv2.Canny(imgBlur,10,50)

#CONTOURS:-
contours,hierarchy=cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
#FINDING RECTANGLE
main.rectContour(contours)
# imgBlank=np.zeros_like(img)
imgArray=([img,imgGray,imgBlur,imgCanny,imgContours])
imgStacked=main.stackImages(imgArray,0.5)
cv2.imshow("Stacked Images",imgStacked)

cv2.waitKey(0)
# cv2.destroyAllWindow()
