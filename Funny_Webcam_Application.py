import cv2
import numpy as np


video_file_capture = cv2.VideoCapture("input\Funny_video.mp4")
webcam_capture = cv2.VideoCapture(0)

ret, webcam_frame = webcam_capture.read()
webcam_height, webcam_width = webcam_frame.shape[:2]
print(webcam_height, webcam_width)

ret, video_frame = video_file_capture.read()
video_height, video_width = video_frame.shape[:2]
print(video_height, video_width)

output_size = (video_width, video_height)

fps = 40
output_video = cv2.VideoWriter(
    "output/Hossein.mp4", cv2.VideoWriter_fourcc(*"XVID"), fps, output_size, False
)
is_paused = False

while True:
    if not is_paused:
        ret, video_frame = video_file_capture.read()

    ret, webcam_frame = webcam_capture.read()
    webcam_resized = cv2.resize(webcam_frame, (video_width + 200, video_height - 200))
    webcam_flipped = cv2.flip(webcam_resized, 1)

    gray_video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
    gray_webcam_frame = cv2.cvtColor(webcam_flipped, cv2.COLOR_BGR2GRAY)

    gray_video_frame[274:424, 130:280] = gray_webcam_frame[274:424, 130:280]

    output_video.write(gray_video_frame)
    cv2.imshow("Video Output", gray_video_frame)

    # Keyboard controls
    key = cv2.waitKey(25) & 0xFF
    if key == ord("s"):
        is_paused = True
    elif key == ord("p"):
        is_paused = False
    elif key == ord("q"):
        break

video_file_capture.release()
webcam_capture.release()
output_video.release()
cv2.destroyAllWindows()
