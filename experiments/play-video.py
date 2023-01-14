import cv2
import time

video = cv2.VideoCapture('../video.mp4')
fps = video.get(cv2.CAP_PROP_FPS)


# CAP_PROP_FRAME_HEIGHT = 4
# CAP_PROP_FRAME_WIDTH = 3

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f'{width=}, {height=}')
cv2.namedWindow("video", 0)
cv2.resizeWindow("video", 320, 200)

# ms = int(1000 / fps * 75 / 100)
ms = 25
print(f'{fps=}, {ms=}')
while video.isOpened():
    success, frame = video.read()
    # ret = video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # print(f'{ret=}')
    # ret = video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # print(f'{ret=}')
    if success:
        cv2.imshow('video', frame)
        if cv2.waitKey(ms) & 0xFF == ord('q'):
            break
    else:
        break


video.release()
cv2.destroyAllWindows()
