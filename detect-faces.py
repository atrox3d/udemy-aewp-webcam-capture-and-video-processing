import cv2
import numpy
import time

import image_helpers

video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)

face_cascade = cv2.CascadeClassifier('faces.xml')

cv2.namedWindow("video", 0)
cv2.resizeWindow("video", 320, 200)

success = True
while success:
    success, frame = video.read()
    if not success:
        break
    # frame = image_helpers.resize(frame, 50)
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    # print(f'{faces=}')

    rectangles = [[x, y, x + w, y + h] for x, y, w, h in faces]
    # print(f'{rectangles=}')

    # target_frame = frame.copy()
    for rectangle in rectangles:
        pt1, pt2 = image_helpers.get_points_from_rectangle(rectangle)
        color = (255, 255, 255)
        cv2.rectangle(frame, pt1, pt2, color, 3)

    # cv2.imshow('original', frame)
    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    # time.sleep(2)
