from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')

    model.train(data='config.yml', epochs=100)
