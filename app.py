import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
  success, image = cap.read()

  cv2.imshow("Image", image)
  cv2.waitKey(1)

