import cv2
import numpy
import numpy as np

# load video
source = cv2.VideoCapture('video-sample.mp4')

# load classifier xml
cascade = cv2.CascadeClassifier('faces.xml')

# get video dimensions
video_width = int(source.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(source.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'{video_width=}, {video_height=}')

# load cat face image
cat: numpy.ndarray = cv2.imread('cat-face.png')
image_height, image_width, _ = cat.shape
print(f'{image_width=}, {image_height=}')

# create output window and resize it
cv2.namedWindow('cats', 0)
cv2.resizeWindow('cats', video_width // 6, video_height // 6)

# loop through the frames
while True:
    success, frame = source.read()
    if not success:
        break

    # detect faces
    faces = cascade.detectMultiScale(frame, 1.1, 4)

    # create list of rectangle from detected faces for this frame
    rectangles = [(x, y, x+w, y+h) for x, y, w, h in faces]

    # draw each rectangle on the current frame
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        pt1, pt2 = (x1, y1), (x2, y2)
        cv2.rectangle(frame, pt1, pt2, (0, 255, 255), 10)

    # show frame
    cv2.imshow('cats', frame)

    # give time do display and detect q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
source.release()
cv2.destroyAllWindows()
