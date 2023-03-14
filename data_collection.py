import os
import time
import cv2
import uuid
import random

try:
    os.mkdir("data")
    for i in ['val','train','test',"images","labels"]:
        os.mkdir(f"data/{i}")
        for j in ["images","labels"]:
            os.mkdir(f"data/{i}/{j}")
except Exception as e:
    print(e)
    
img_path=os.path.join("data","images")
number_images=90

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    