#########################################
#  We will use this file if we want     #
#    to collect the data                #
#    using our own webcam               #
# we will use thi code for getting empty#
#########################################


# Importing the libraries
import os
import time
import cv2
import uuid
import random


# Creating the necessary files in the project
try:
    os.mkdir("facial_recognition/data")
    for i in ['val', 'train', 'test', "images", "labels"]:
        os.mkdir(f"facial_recognition/data/{i}")
        for j in ["images", "labels"]:
            if i not in ["images", "labels"]:
                os.mkdir(f"facial_recognition/data/{i}/{j}")
except Exception as e:
    print(e)

# path of the data
img_path = os.path.join("facial_recognition","data", "images")

number_images = 60

cap = cv2.VideoCapture(0)

for i in range(number_images):
    _, frame = cap.read()
    # writing the images
    cv2.imwrite(os.path.join(img_path, f"{str(uuid.uuid1())}.jpg"), frame)
    cv2.imshow("Collecting Data", frame)
    time.sleep(0.5)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
