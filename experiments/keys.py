import cv2

img = cv2.imread('../images/01.jpg')
img = cv2.resize(img, (640, 480))
while True:
    cv2.imshow('out', img)
    key = cv2.waitKey(0)
    key0xff = key & 0xFF
    print(f'{key=}, {key=:b}, {0xFF=:b}, {0x00FF=:b}, {ord("q")=}, {ord("q")=:b}')
    print(f'{512=:b}')
    if key & 0xFF == ord('q'):
        break
