import cv2
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
print(major_ver, minor_ver, subminor_ver)
