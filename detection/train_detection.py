from ultralytics import YOLO

if __name__ == '__main__':
    # Load a pretrained YOLO model (recommended for training)
    model = YOLO("yolo11l.pt")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    results = model.train(data=r'dataset\data.yaml', epochs=500)