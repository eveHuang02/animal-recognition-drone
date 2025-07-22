# Animal Detection Model Training

This module trains a YOLOv8–YOLOv11 object detection model to locate animals in drone-captured images.

## Folder Contents

- `detection_dataset/`: Contains the dataset organized into `train`, `val`, and `test` subsets with images and YOLO-format labels.
- `split.py`: Script to split the dataset into training, validation, and test sets.
- `train_detection.py`: Script to train the YOLO object detection model.
- `results/`: Stores the trained weights and logs.

## Step 1: Split the Detection Dataset

Use the following command to split the dataset:

```bash
python split.py
```

This creates the `train`, `val`, and `test` folders inside `detection_dataset/`.

## Step 2: Train the Detection Model

Use the following command to train the YOLO detection model:

```bash
python train_detection.py
```

The best model weights will be saved in:

```
results/train/weights/best.pt
```

**Note:** The dataset has already been split. Only a minimal sample is retained in `detection_dataset/train` for confidentiality.
