import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("frame", frame)
	cv2.imshow("gray",gray)
	if (cv2.waitKey(3000) & 0xFF == ord('q')):
		break

cv2.destroyAllWindows()
cap.release()

