import cv2
import numpy as np
import Utility

widthimg = 700
heightimg = 700
questions = 5
choices = 5
ans = [1,3,3,3,1]

img = cv2.imread("omrM1.png")
imgContours = img.copy()
imgBiggestContour = img.copy()

#Img Processing
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting image into grey scale
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)#Bluring the image
imgCanny = cv2.Canny(imgBlur,10,50)

#Finding all coutours
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,contours,-1,(0,255,0),3)

#Find Rectangles
rectCon = Utility.rectCountour(contours)
#biggestContour = Utility.getCornerPoints(rectCon[0])
#print(biggestContour)

#if(biggestContour.size !=0):
    #cv2.drawContours(imgBiggestContour,biggestContour,-1,(0,255,0),5)

#Applying Threshold
imgThresh = cv2.threshold(imgGray,170,255,cv2.THRESH_BINARY_INV)[1]
boxes = Utility.splitBoxes(imgThresh)
#cv2.imshow("Test",boxes[2])
#print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[1]))

#Getting Non Zero Pixel Values of each box
myPixVal = np.zeros((questions,choices))
col = 0
row = 0
for image in boxes:
    totalPix = cv2.countNonZero(image)
    myPixVal[row][col] = totalPix
    col+=1
    if(col == choices):
        row+=1
        col = 0
#print(myPixVal)

#Getting the index of marking
myIndex = []
for x in range(0,questions):
    arr = myPixVal[x]
    myIndexVal = np.where(arr==np.amax(arr))
    #print(myIndexVal[0][0])
    myIndex.append(int(myIndexVal[0][0]))
print(myIndex)

#Grading
grading = []
for x in range(0,questions):
    if ans[x]==myIndex[x]:
        grading.append(1)
    else: grading.append(0)

score = (sum(grading)/questions)*100 #Final Grade
print(score)

imgResult = img.copy()
imgResult = Utility.showAnswer(imgResult,myIndex,grading,ans,questions,choices)
imgScore = img.copy()
cv2.putText(imgScore,str(int(score))+"%",(int(img.shape[1]/questions)*1,int(img.shape[0]/choices)*3),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)

imgBlank = np.zeros_like(img)#A Blank Image
imageArray = ([img,imgGray,imgBlur,imgCanny],
              [imgContours,imgThresh,imgResult,imgScore])
imgStacked = Utility.stackImages(imageArray,1)

cv2.imshow("Orignal",imgStacked)
cv2.waitKey(0)