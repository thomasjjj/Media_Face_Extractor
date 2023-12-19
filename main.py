import dlib
import cv2
import numpy as np
import os
from tqdm import tqdm


# Initialize Dlib's face detector
detector = dlib.get_frontal_face_detector()

def extract_faces(frame, buffer=0.2):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Adjust the face coordinates to include a wider area
    adjusted_faces = []
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        x_buffer = int(w * buffer)
        y_buffer = int(h * buffer)

        x_start = max(0, x - x_buffer)
        y_start = max(0, y - y_buffer)
        x_end = min(frame.shape[1], x + w + x_buffer)
        y_end = min(frame.shape[0], y + h + y_buffer)

        cropped_face = frame[y_start:y_end, x_start:x_end]
        adjusted_faces.append(cropped_face)

    return adjusted_faces

def process_video(video_path, output_folder):
    # Check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    with tqdm(total=total_frames, desc="Processing Video") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Select key frames (e.g., every 10th frame)
            if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % 10 == 0:
                faces = extract_faces(frame)
                # Save faces in the output folder
                for i, face in enumerate(faces):
                    face_filename = f'{output_folder}/face_{int(cap.get(cv2.CAP_PROP_POS_FRAMES))}_{i}.jpg'
                    cv2.imwrite(face_filename, face)

            pbar.update(1)

    cap.release()

def safe_path(input_path):
    return input_path.replace('\\', '\\\\')

print('')
print('############################################################')
print('When entering file paths, make sure there are no quote marks')
print('############################################################')
print('')

videopath = input('Add file path to the video: ')
outputpath = input('Add filepath to the output folder: ')

# Process the paths to ensure they are safe for use
safe_videopath = safe_path(videopath)
safe_outputpath = safe_path(outputpath)

process_video(safe_videopath, safe_outputpath)
