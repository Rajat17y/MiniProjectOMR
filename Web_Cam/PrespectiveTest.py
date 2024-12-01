import cv2
import numpy as np

# Capture a frame from the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Define four points for perspective transform
        # These should be corners of the warped region in the original image
        pts1 = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

        # Get the perspective transform matrix
        matrix = cv2.getPerspectiveTransform(pts1, pts2)

        # Warp the perspective
        warped = cv2.warpPerspective(frame, matrix, (300, 300))

        # Modify the warped image (e.g., add text)
        cv2.putText(warped, "Hello", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Get the inverse perspective transform matrix
        inverse_matrix = cv2.getPerspectiveTransform(pts2, pts1)

        # Warp the modified image back to original perspective
        inverse_warped = cv2.warpPerspective(warped, inverse_matrix, (frame.shape[1], frame.shape[0]))

        # Combine the inverse-warped image with the original frame
        # Use a mask to overlay only the modified region
        #mask = np.zeros_like(frame, dtype=np.uint8)
        #cv2.fillConvexPoly(mask, np.int32(pts1), (255, 255, 255))
        blended = cv2.addWeighted(frame, 1, inverse_warped, 1, 0)

        # Show the result
        cv2.imshow("Warped", warped)
        cv2.imshow("Result", blended)

        # Exit loop on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
