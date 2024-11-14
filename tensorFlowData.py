import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import tensorflow as tf
DATADIR = "Digits"
training = []
count = 0
# x_train = tf.keras.utils.normalize(x_train, axis = 1)
# x_test = tf.keras.utils.normalize(x_test, axis = 1)
for image in os.listdir(DATADIR):
    nums = np.array(Image.open(os.path.join(DATADIR, image)))
    plt.imshow(nums, cmap = "gray")
    training.append([nums, count % 10])
    count += 1

X = []
Y = []
for xIm, yIm in training:
    X.append(xIm)
    Y.append(yIm)

np.save("X", X)
np.save("Y", Y)

x_digits = np.load("X.npy")
y_digits = np.load("Y.npy")


# plt.imshow(training[1][0])


# image identifying through tf:

#print(x_train[0])