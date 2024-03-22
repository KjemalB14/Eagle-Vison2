from ultralytics import YOLO
import cv2
import math
from gpiozero import LED
import time

# Setup GPIO
led = LED(17)

#start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO("/home/ENKH/Desktop/Senior_cap/runs/detect/train2/weights/best.pt")

classNames = ["Enemy", "People"]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

   # coordinates
    for r in results:
        boxes = r.boxes
        enemy_detected = False
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # Determine color based on class
            cls = int(box.cls[0])
            if cls == 0:  # Enemy
                color = (0, 0, 255)  # Red
                enemy_detected = True
            elif cls == 1:  # People
                color = (0, 255, 0)  # Green

            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100

            # class name
            cls = int(box.cls[0])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, (255, 255, 255), thickness)  # White text

                # Control the LED based on enemy detection
            if enemy_detected:
                led.on()  # Turn on LED
            else:
                led.off()  # Turn off LED


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()