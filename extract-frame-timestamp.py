import cv2
import numpy
from pathlib import Path

import image_helpers
import time_helpers


# get video
video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)

# set/create images path
images = Path('images/')
images.mkdir(exist_ok=True)

# get video stats
fps = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
length_seconds = frame_count / fps
print(f'{frame_count}, {fps=}, {length_seconds=}')

timestamp = '00:00:01.88'
while True:
    # convert timestamp to seconds
    total_seconds = time_helpers.timestamp2seconds(timestamp)
    frame_nr = total_seconds * fps
    print(f'{frame_nr=}')

    # set current frame
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_nr)

    # get current frame and resize it
    success, frame = video.read()
    if not success or total_seconds < 0.0:
        print(f'ERROR | !success | {total_seconds=}')
        if total_seconds >= length_seconds:
            timestamp = time_helpers.seconds2timestamp(length_seconds - 0.01)
        elif total_seconds < 0.0:
            timestamp = time_helpers.seconds2timestamp(0.0)
        continue
    print(f'success | {total_seconds=}')

    frame = image_helpers.resize(frame, 50)

    # create window title
    height, width, _ = frame.shape
    title = f'{timestamp}, {round(frame_nr, 1)} @{width}x{height}'

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
    cv2.imshow('output', frame)

    key = cv2.waitKey(0)
    print(key)

    match key:
        case 113:
            break
        case 119:
            timestamp = time_helpers.seconds2timestamp(total_seconds + 1)
        case 115:
            timestamp = time_helpers.seconds2timestamp(total_seconds - 1)
        case 100:
            timestamp = time_helpers.seconds2timestamp(total_seconds + 0.01)
        case 97:
            timestamp = time_helpers.seconds2timestamp(total_seconds - 0.01)

    # cv2.destroyAllWindows()
