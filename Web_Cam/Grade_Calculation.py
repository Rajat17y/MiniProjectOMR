import cv2
import numpy as np


def showAnswer(img,myIndex,grading,ans,questions,choices):
    secW = int(img.shape[1]/choices)
    secH = int(img.shape[0]/questions)

    for x in range(0,questions):
        myAns = myIndex[x]
        cX = (myAns*secW)+secW//2
        cY = (x*secH)+secH//2
        if grading[x]==1:
            mycolor = (0,255,0)
        else:
            mycolor = (0,0,255)
            cXR = (ans[x]*secW)+secW//2
            cv2.circle(img,(cXR,cY),18,(0,255,0),cv2.FILLED)
        cv2.circle(img,(cX,cY),18,mycolor,cv2.FILLED)
    return img

def splitBoxes(img,questions,choices):
    rows = np.array_split(img,questions,axis=0)
    boxes = []
    for r in rows:
        cols = np.array_split(r,choices,axis=1)
        for box in cols:
            boxes.append(box)
    return boxes

def detect(imgGray,questions,choices):
    #imgThresh = cv2.threshold(imgGray,170,255,cv2.THRESH_BINARY_INV)[1]
    imgThresh = cv2.adaptiveThreshold(
    imgGray, 255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY_INV, 
    29, 5)
    boxes = splitBoxes(imgThresh,questions,choices)
    #cv2.imshow("Thresh",imgThresh)
    #cv2.imshow("Test",boxes[2])
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

def grading(dected,ans,questions):
    grading = [0]*len(ans)
    for x in range(0,questions):
        if ans[x]==dected[x]:
            grading[x] = 1
        else: grading[x]=0
    return grading

def score(dected,ans,questions):
    grading = []
    for x in range(0,questions):
        if ans[x]==dected[x]:
            grading.append(1)
        else: grading.append(0)
    score = (sum(grading)/questions)*100 #Final Grade
    return score

def textScreen(frame,text,rect_top_left,rect_bottom_right):
        # Define the text to display
        #text = "Hello, OpenCV!"
        
        # Calculate the position for the text (center it in the rectangle)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        thickness = 2
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = rect_top_left[0] + (rect_bottom_right[0] - rect_top_left[0] - text_size[0]) // 2
        text_y = rect_top_left[1] + (rect_bottom_right[1] - rect_top_left[1] + text_size[1]) // 2

        cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 255, 0), thickness)