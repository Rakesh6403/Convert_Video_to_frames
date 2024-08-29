import cv2
import os

def video_to_frames(video_file, output_folder):
    # Read the video file
    cap = cv2.VideoCapture(video_file)
    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize frame count
    frame_count = 0

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Save frame as JPEG file
            frame_file = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_file, frame)
            frame_count += 1
        else:
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()


# Example usage:
video_file = 'path/to/video.mp4'  # Replace with your video file path
output_folder = 'saved_frames'  # Replace with the folder where frames will be saved

video_to_frames(video_file, output_folder)