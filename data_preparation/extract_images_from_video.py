import os
import subprocess
import cv2

# Function to extract frames from videos
def frame_capture(input_video, output_folder):
    cap = cv2.VideoCapture(input_video)
    currentframe = 0
    i = 0 # For naming files
    fps = round(cap.get(cv2.CAP_PROP_FPS))
    # fps = 30

    # Check if the video is opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file {input_video}")
        return

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read and save frames
    while True:
        ret, frame = cap.read()

        if currentframe % fps== 0:
            # Save the current frame
            frame_name = os.path.join(output_folder, f'cattle_1_{i}.jpg')
            print(f'Creating... {frame_name}')
            cv2.imwrite(frame_name, frame)
            i += 1
        currentframe += 1  # Increment frame count

        if not ret:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("All videos have been processed.")

if __name__ == '__main__':
    input_video = os.path.join("videos", "cattle", "Cattle.ts")
    output_folder = os.path.join("images", "cattle", "cattle_1")
    
    # Call the frame capture function
    frame_capture(input_video=input_video, output_folder=output_folder)