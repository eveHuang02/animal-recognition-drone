from ultralytics import YOLO

if __name__ == '__main__':
    # Load a pretrained YOLO model (recommended for training)
    model = YOLO("yolo11n-cls.pt")

    # Train the model
    results = model.train(data=r"classification_dataset", epochs=500, imgsz=640)