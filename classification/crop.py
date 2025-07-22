import os
import cv2

# Path to the folder containing images and label files
image_folder = r"detection_dataset/train/images"
label_folder = r"detection_dataset/train/labels"

# Directories for cropped images based on object categories
crop_dir = "classification_dataset"
pig_dir = "classification_dataset/pig"
deer_dir = "classification_dataset/deer"
roo_dir = "classification_dataset/roo"

# Ensure directories exist
os.makedirs(pig_dir, exist_ok=True)
os.makedirs(deer_dir, exist_ok=True)
os.makedirs(roo_dir, exist_ok=True)

# Loop through all images in the image folder
for image_name in os.listdir(image_folder):
    if image_name.endswith('.jpg'):  # Ensure .jpg files
        image_file = os.path.join(image_folder, image_name)
        
        # Find the corresponding label file (assuming label file has the same name as the image)
        label_name = image_name.replace('.jpg', '.txt')
        label_file = os.path.join(label_folder, label_name)
        
        # Ensure the label file exists
        if not os.path.exists(label_file):
            print(f"Label file not found for {image_name}, skipping.")
            continue
        
        # Read the image
        img = cv2.imread(image_file)
        height, width, _ = img.shape  # Get image dimensions
        
        # Read the label file
        with open(label_file) as file:
            lines = file.readlines()
        
        # Process each bounding box in the label file
        for idx, line in enumerate(lines):
            class_id, x, y, w, h = map(float, line.split())
            
            # Scale YOLO coordinates to pixel values
            class_id = int(class_id)
            x_center = int(x * width)
            y_center = int(y * height)
            box_width = int(w * width)
            box_height = int(h * height)
            
            # Calculate top-left and bottom-right corners
            x_min = max(0, x_center - box_width // 2)
            y_min = max(0, y_center - box_height // 2)
            x_max = min(width, x_center + box_width // 2)
            y_max = min(height, y_center + box_height // 2)

            # Crop the image
            crop = img[y_min:y_max, x_min:x_max]

            # Determine the appropriate crop directory based on the object class
            if image_name.startswith('pig'):
                crop_filename = os.path.join(pig_dir, f"{image_name.replace('.jpg', '')}_{idx}.jpg")
            elif image_name.startswith('deer'):
                crop_filename = os.path.join(deer_dir, f"{image_name.replace('.jpg', '')}_{idx}.jpg")
            elif image_name.startswith('roo'):
                crop_filename = os.path.join(roo_dir, f"{image_name.replace('.jpg', '')}_{idx}.jpg")
            else:
                print(f"Unknown object type for {image_name}, skipping.")
                continue

            # crop_filename = os.path.join(crop_dir, f"{image_name.replace('.jpg', '')}_{idx}.jpg")

            # Save the cropped image
            h, w, _ = crop.shape

            crop_rs = cv2.resize(crop, (512,int(h*(512/w))))
            cv2.imwrite(crop_filename, crop_rs)
            print(f"Cropped image saved as {crop_filename}")
