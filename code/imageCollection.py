import cv2 
import uuid
import time

#import os
#from picamera2 import Picamera2, Preview
#from libcamera import controls
#import libcamera


#Images to collect
labels = ['square', 'circle', 'triangle']
number_imgs = 3

#Set camera object
#picam2 = Picamera2()

camera = cv2.VideoCapture(0)

#for i in range(number_imgs):
#time.sleep(2)
ret, frame = camera.read()
    #if ret:
        # Save the image with a unique filename
image_filename = f"/home/ENKH/Senior Project/Eagle-Vison2/Tensorflow/workspace/images/collectedimages/triangle/image_trianlge11p.jpg"
cv2.imwrite(image_filename, frame)
        #print(f"Image {i+1} captured: {image_filename}")

        # Show the captured image
cv2.imshow("Captured Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release the camera
camera.release()

















#Sets camera configuration (Idk all settings)
#camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
#camera_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
#picam2.configure(camera_config)

#Brings up preview window, starts the camera up, waits 2 seconds, takes a picture called 'test.jpg'
#in file path /home/ENKH/Senior Project/Eagle-Vison2/test.jpg
#picam2.start_preview(Preview.QTGL)
#picam2.start()
#picam2.set_controls({"AfMode": controls.AfModeEnum.Auto})
#time.sleep(10)
#picam2.capture_file("test.jpg")

#Puts image into variable
#image = cv2.imread("/home/ENKH/Senior Project/Eagle-Vison2/test.jpg")

#Shows image in CV window
#cv2.imshow("Test Image", image)
#cv2.waitKey(0)



