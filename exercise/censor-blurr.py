import cv2
import numpy as np

import image_helpers

video = cv2.VideoCapture('smile.mp4')
video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

face_cascade = cv2.CascadeClassifier('faces.xml')

codec = cv2.VideoWriter_fourcc(*'H264')
output = cv2.VideoWriter('smile-blur.mp4', codec, 30, (video_width, video_height))

if SHOW_VIDEO := True:
    cv2.namedWindow('out', 0)
    cv2.resizeWindow('out', video_width // 2, video_height // 2)

count = 0
while True:
    frame: np.ndarray
    success: bool
    success, frame = video.read()
    if not success:
        break
    count += 1
    #
    #
    #
    # detect faces
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    # create list of rectangle from detected faces for this frame
    rectangles = [(x, y, x+w, y+h) for x, y, w, h in faces]
    print(f'frame {count}/{frame_count}: {rectangles=}')
    for x1, y1, x2, y2 in rectangles:
        blur = cv2.blur(frame[y1:y2, x1:x2], (50, 50))
        frame[y1:y2, x1:x2] = blur
    #
    #
    #
    if SHOW_VIDEO:
        cv2.imshow('out', frame)
    output.write(frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
