import cv2
import numpy as np

def frame_difference(prev_frame, curr_frame, threshold=100000):
    diff = cv2.absdiff(prev_frame, curr_frame)
    non_zero_count = np.sum(diff > 50)
    return non_zero_count > threshold

def save_frames_on_change(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    ret, prev_frame = cap.read()
    if not ret:
        print("Failed to read video")
        return
    prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if frame_difference(prev_frame, gray_frame):
            frame_count += 1
            cv2.imwrite(f"{output_folder}/frame_{frame_count}.jpg", frame)
        prev_frame = gray_frame

    cap.release()

video_path = 'vid.mp4'
output_folder = 'photos'
save_frames_on_change(video_path, output_folder)
