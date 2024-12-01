import cv2
import numpy as np
import Grade_Calculation as gc

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


# Reorder points for perspective transformation
def reorderPoints(pts):
    pts = pts.reshape((4, 2))  # Reshape to (4, 2)
    rect = np.zeros((4, 2), dtype=np.float32)

    # Sum and difference to find corners
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    rect[0] = pts[np.argmin(s)]  # Top-left
    rect[2] = pts[np.argmax(s)]  # Bottom-right
    rect[1] = pts[np.argmin(diff)]  # Top-right
    rect[3] = pts[np.argmax(diff)]  # Bottom-left

    return rect

def inv_matrix(frame, points):
    # Reorder points
    points = reorderPoints(points)

    # Define the desired perspective rectangle size
    width = 400
    height = 300
    dst = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype=np.float32)

    # Get perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(dst,points)
    return matrix

# Perspective transformation for biggest rectangle
def warpPerspective(frame, points):
    # Reorder points
    points = reorderPoints(points)

    # Define the desired perspective rectangle size
    width = 400
    height = 300
    dst = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype=np.float32)

    # Get perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(points, dst)

    # Perform the perspective warp
    return cv2.warpPerspective(frame, matrix, (width, height))

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
                x, y, w, h = cv2.boundingRect(biggest)  # Get bounding rectangle
                cv2.rectangle(rect_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)# Draw rectangle here

                warped = warpPerspective(frame, biggest)
                warpedRaw = np.zeros_like(warped)
                warped_Gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
                warpedRaw = gc.showAnswer(warpedRaw,gc.detect(warped_Gray),gc.grading(gc.detect(warped_Gray),[4,3,4,2,1]),[4,3,4,2,1],5,5)
                cv2.imshow("Warped Perspective", warped) #Prespective view

                #Inverse
                inverse_warped = cv2.warpPerspective(warpedRaw,inv_matrix(frame,biggest),(frame.shape[1], frame.shape[0]))
                blended = cv2.addWeighted(frame, 1, inverse_warped, 1, 0)
                cv2.imshow('Merge',blended)
                #print(gc.detect(warped_Gray))
                cv2.imshow("Gray",warped_Gray)
                
                #Score Calculation
                print(gc.score(gc.detect(warped_Gray),[4,3,4,2,1]))
                gc.textScreen(rect_frame,str(gc.score(gc.detect(warped_Gray),[4,3,4,2,1])),(x,y),(x + w, y + h))

                #print("Yes")
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
