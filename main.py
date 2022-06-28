import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = './photos'

training_data = []

for img in os.listdir(path):
    pic = cv2.imread(os.path.join(path,img))
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic,(250,250))
    training_data.append([pic])

np.save(os.path.join(path,'photos'),np.array(training_data))
saved = np.load(os.path.join(path,'photos.npy'))