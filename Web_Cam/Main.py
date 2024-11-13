import cv2
import numpy as np

#finding_Countours
def rectContours(cont):
    rectC = []
    for i in cont:
        area = cv2.contourArea(i)
        if area>50:
            peri = cv2.arcLength(i,True)#Detect closed arclength
            approx = cv2.approxPolyDP(i,0.02*peri,True)#findind contour points
            if(len(approx)==4):
                rectC.append(i)
    rectC = sorted(rectC,key=cv2.contourArea,reverse=True)
    return rectC

def getCorner(cont):
    peri = cv2.arcLength(cont,True)
    approx = cv2.approxPolyDP(cont,0.02*peri,True)
    return approx

# Open the default camera (usually webcam at index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame was read successfully
        if ret:
            # Display the resulting frame
            contour_frame = frame.copy()
            rect_frame = frame.copy()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur_frame = cv2.GaussianBlur(gray_frame,(5,5),1)
            canny_frame = cv2.Canny(blur_frame,10,50)
            #Detecting_Countours
            contours,hierarchy = cv2.findContours(canny_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            rectCon = rectContours(contours)
            biggest = []
            if(len(rectCon)!=0):
                biggest = getCorner(rectCon[0])
                #print("Yes")
            if(len(biggest)!=0):
                cv2.drawContours(rect_frame,biggest,-1,(0,255,0),10)
                print("Yes")
            #cv2.drawContours(rect_frame,contours,-1,(0,255,0),1)

            cv2.imshow('Webcam', rect_frame)

            # Break the loop when 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not read frame.")
            break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
