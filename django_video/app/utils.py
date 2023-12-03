import cv2
import numpy as np


def main_func(string: str):
    pict = np.zeros((100, 100, 3), dtype=np.uint8)
    text = string
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = 1
    text_color = (255, 105, 180)
    line = cv2.LINE_AA
    fps = 30
    video_length = 3
    frames = fps * video_length
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('3_sec_video.mp4', fourcc, fps, (100, 100))
    f = 1
    for frame in range(frames):
        pict.fill(0)
        text_x = (cv2.getTextSize(text, font, text_size, f)[0])[0]
        text_y = (cv2.getTextSize(text, font, text_size, 1)[0])[1]
        x = 100 + 10*len(text) - text_x
        y = (100 + text_y) // 2
        cv2.putText(pict, text, (x, y), font, text_size, text_color, 1, line)
        video_writer.write(pict)
        f += 1
    video_writer.release()
    return
