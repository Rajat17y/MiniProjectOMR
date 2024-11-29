import cv2
import numpy as np

questions = 5
choices = 5

def splitBoxes(img):
    rows = np.array_split(img,questions,axis=0)
    boxes = []
    for r in rows:
        cols = np.array_split(r,choices,axis=1)
        for box in cols:
            boxes.append(box)
    return boxes

def detect(imgGray):
    #imgThresh = cv2.threshold(imgGray,170,255,cv2.THRESH_BINARY_INV)[1]
    imgThresh = cv2.adaptiveThreshold(
    imgGray, 255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY_INV, 
    29, 5)
    boxes = splitBoxes(imgThresh)
    cv2.imshow("Thresh",imgThresh)
    cv2.imshow("Test",boxes[2])
    #Getting NonZero Pixel Values of each box
    myPixVal = np.zeros((questions,choices)) #rows = question and columns = choices
    col = 0
    row = 0
    for image in boxes:
        totalPix = cv2.countNonZero(image)
        myPixVal[row][col] = totalPix
        col+=1
        if(col == choices):
            row+=1
            col = 0

    #Getting the index of marking
    myIndex = []
    for x in range(0,questions):
        arr = myPixVal[x]
        myIndexVal = np.where(arr==np.amax(arr))
        #print(myIndexVal[0][0])
        myIndex.append(int(myIndexVal[0][0]))
    return myIndex

def score(dected,ans):
    grading = []
    for x in range(0,questions):
        if ans[x]==dected[x]:
            grading.append(1)
        else: grading.append(0)
    score = (sum(grading)/questions)*100 #Final Grade
    return score