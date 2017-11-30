import pickle
import random
import matplotlib.pyplot as plt
import numpy as np
import cv2
import yaml


root_dir = "/media/torben/0F5F0A370F5F0A37/Dokumente/Unterlagen/Udacity/Self-Driving-Car-ND/Term3/CarND-Capstone/training/Bosch_dataset_rgb/"
target_dir = "/media/torben/0F5F0A370F5F0A37/Dokumente/Unterlagen/Udacity/Self-Driving-Car-ND/Term3/CarND-Capstone/training/Bosch_dataset_rgb/crop/"

with open(root_dir + "train.yaml", 'r') as stream:
    data = yaml.load(stream)
    print("YAML File loaded ! Found " + str(len(data)) + " Entries")



for i in range(0,len(data)):
    if data[i]["boxes"]:
        for j in range(0,len(data[i]["boxes"])):
            label = data[i]["boxes"][j]["label"]
            img = cv2.imread(root_dir + data[i]["path"])
            crop_img = img[round(data[i]["boxes"][j]["y_min"]):round(data[i]["boxes"][j]["y_max"]),
                       round(data[i]["boxes"][j]["x_min"]):round(data[i]["boxes"][j]["x_max"]), :]
            filename = data[i]["path"][1:].split('/')[-1].split('.')[0] + "_" + str(j) + ".png"
            if crop_img.shape[0] > 0 and crop_img.shape[1] > 0:
                if label == "Green":
                    cv2.imwrite(target_dir + "green/" + filename, crop_img)
                elif label=="Yellow":
                    cv2.imwrite(target_dir + "yellow/" +  filename, crop_img)
                elif label=="Red":
                    cv2.imwrite(target_dir + "red/" +  filename, crop_img)


print("Images cropped and labelled !")

