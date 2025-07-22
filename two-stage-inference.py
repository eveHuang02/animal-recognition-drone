from ultralytics import YOLO
import cv2
import os


# Load the object detection model
od_model = YOLO(r'detection\results\train\weights\best.pt')

# Load the image classification model
ic_model = YOLO(r'classification\results\train\weights\best.pt')

# Load video
video_path = r"data_preparation\videos\deer_and_kangaroo\deer_and_roo_1.ts"
cap = cv2.VideoCapture(video_path)

# Check if video is opened correctly
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Resize resolution to desired output size 
output_resolution = (1280, 720)

# Initialize the video writer with the same resolution
output = cv2.VideoWriter("pig.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, output_resolution)

# Read until video is completed
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Resize the frame to match the output resolution
        frame_resized = cv2.resize(frame, output_resolution)

        # Run object detection
        od_results = od_model(frame_resized)

        # Iterate over detection results
        for det in od_results[0].boxes.xyxy:
            # Extract bounding box coordinates
            x1, y1, x2, y2 = map(int, det[:4])

            # Crop the detected region
            crop_img = frame_resized[y1:y2, x1:x2]

            # Run image classification on the cropped image
            cls_results = ic_model(crop_img)
            acc = cls_results[0].probs.top5conf[0]

            # Get classification label (assuming top-1 classification)
            label = cls_results[0].probs.top1
            class_name = ic_model.names[label]

            if acc > 0.8:
                if class_name == 'deer':
                    color = (128, 0, 0)  # blue for 'deer'
                elif class_name == 'roo':
                    color = (0, 128, 128)  # Yellow for 'roo'
                elif class_name == 'pig':
                    color = (0, 128, 0)  # blue for 'pig'

                # Draw the bounding box and label on the frame
                cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 1)
                cv2.putText(frame_resized, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1, cv2.LINE_AA)

        # cv2.imshow("img", frame_resized)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        # Write the processed frame to the output video
        output.write(frame_resized)

    else:
        break

# Release resources when done
cap.release()
output.release()

# Close all OpenCV windows
cv2.destroyAllWindows()








