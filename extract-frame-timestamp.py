import cv2
import numpy
from pathlib import Path

import image_helpers

# get video
video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)

# set/create images path
images = Path('images/')
images.mkdir(exist_ok=True)

# get video stats
fps = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
print(f'{frame_count}, {fps=}')

# convert timestamp to seconds
timestamp = '00:00:01.88'
hours, minutes, seconds = [float(n) for n in timestamp.split(':')]
total_seconds = hours * 3600 + minutes * 60 + seconds
frame_nr = total_seconds * fps
print(f'{timestamp=}, {hours=}, {minutes=}, {seconds=}, {total_seconds=}, {frame_nr=}')

# set current frame
video.set(cv2.CAP_PROP_POS_FRAMES, frame_nr)

# get current frame and resize it
success, frame = video.read()
frame = image_helpers.resize(frame, 50)

# create window title
height, width, _ = frame.shape
title = f'{timestamp}, {frame_nr} @{width}x{height}'

# add text to frame
cv2.putText(
    img=frame,
    text=title,
    org=(0, 25),
    fontFace=cv2.FONT_ITALIC,
    fontScale=1,
    color=(255, 255, 255),
    thickness=2,
    lineType=cv2.LINE_AA
)

# show current frame in window
cv2.imshow(title, frame)
cv2.waitKey(0)
