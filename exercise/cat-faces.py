import cv2
import numpy as np


source = cv2.VideoCapture('video-sample.mp4')
cascade = cv2.CascadeClassifier('faces.xml')

width = int(source.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(source.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow('cats', 0)
cv2.resizeWindow('cats', width // 6, height // 6)

while True:
    success, frame = source.read()
    if not success:
        break

    faces = cascade.detectMultiScale(frame, 1.1, 4)
    rectangles = [(x, y, x+w, y+h) for x, y, w, h in faces]
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        pt1, pt2 = (x1, y1), (x2, y2)
        cv2.rectangle(frame, pt1, pt2, (0, 255, 255), 10)
    cv2.imshow('cats', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

source.release()
cv2.destroyAllWindows()
