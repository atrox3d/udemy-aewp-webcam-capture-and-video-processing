import cv2
import time

video = cv2.VideoCapture('../video.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
# ms = int(1000 / fps * 75 / 100)
ms = 25
print(f'{fps=}, {ms=}')

while True:
    start_time = time.time()
    while video.isOpened():
        success, frame = video.read()
        if success:
            cv2.imshow('video', frame)
            if cv2.waitKey(ms) & 0xFF == ord('q'):
                break
        else:
            break

    end_time = time.time()
    elapsed = end_time - start_time
    print("total time taken this loop: ", elapsed)

    if elapsed > 3:
        ms -= 1
    elif elapsed < 3:
        ms += 1
    else:
        break
    print(f'{ms=}')
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
