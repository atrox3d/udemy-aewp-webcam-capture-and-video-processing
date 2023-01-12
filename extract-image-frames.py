import cv2
import numpy
from pathlib import Path
import shutil

video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)

images = Path('images/')
shutil.rmtree(images.__str__(), ignore_errors=True)
images.mkdir(exist_ok=True)

count = 0
success, frame = video.read()
while success:
    count += 1
    path = images / f'{count:02}.jpg'
    cv2.imwrite(path.__str__(), frame)
    success, frame = video.read()

