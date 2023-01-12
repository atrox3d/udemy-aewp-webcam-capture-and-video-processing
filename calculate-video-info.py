import cv2
import numpy

video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
frame_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)
seconds = frame_count / fps
print(f"""
{video_path=}
{width=}, {height=}
{frame_width=}, {frame_height=}
{frame_count=}, {fps=}, {seconds=}
""")
