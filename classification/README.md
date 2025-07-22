# Animal Classification Model Training

This module trains a YOLOv8–YOLOv11 image classification model to categorize detected animals in drone-captured images.

## Folder Contents

- `detection_dataset/`: Contains YOLO-format labeled images used for cropping.
- `classification_dataset/`: Contains cropped and split datasets organized into `train`, `val`, and `test`.
- `crop.py`: Script to crop animal regions from the detection dataset.
- `split.py`: Script to split cropped images into training, validation, and test sets.
- `train_classification.py`: Script to train the YOLO image classification model.
- `results/`: Stores trained model weights and logs.

## Step 1: Build the Classification Dataset

Run the following command to crop the animal images:

```bash
python crop.py
```

This generates a `cropped_images/` folder with class-specific subfolders (e.g., `deer`, `pig`, `roo`).

## Step 2: Split the Classification Dataset

Use the following command to split the cropped images:

```bash
python split.py
```

This creates:

```
classification_dataset/
├── train/
├── val/
└── test/
```

## Step 3: Train the Classification Model

Use the following command to train the YOLO classification model:

```bash
python train_classification.py
```

The best model checkpoint will be saved in:

```
results/train/weights/best.pt
```

**Note:** The dataset in the `classification_dataset` folder has already been split. To maintain data confidentiality, only a single example is retained in `classification_dataset/train`.  
