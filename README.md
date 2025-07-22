# Animal Recognition Using Drone Imaging

This project provides a complete AI pipeline to detect and classify animals such as pigs, kangaroos, and deer from drone-captured videos. It consists of two main modules: object detection and image classification, both based on YOLOv8 to YOLOv11 models.

## Folder Overview

- `data_preparation/`: Tools to extract frames from drone videos.
- `detection/`: Scripts and datasets for training YOLO detection models.
- `classification/`: Scripts and datasets for training YOLO classification models.
- `two-stage-inference.py`: Script that runs the full pipeline for inference.

## Setup Instructions

Create a virtual environment and install the required dependencies:

```bash
conda create --name animal_env python=3.10
conda activate animal_env

pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
pip install ultralytics opencv-python
```

## Extract Frames from Videos

Navigate to the data preparation folder and run:

```bash
cd data_preparation
python extract_images_from_video.py
```

## Train Detection Model

```bash
cd detection
python split.py
python train_detection.py
```

## Train Classification Model

```bash
cd classification
python crop.py
python split.py
python train_classification.py
```

## Run Inference

After training, return to the root folder and run:

```bash
python two-stage-inference.py
```

This will load the trained detection and classification models and perform inference on a specified video file.

**Note:** Pretrained YOLO models must be downloaded or provided before training.
