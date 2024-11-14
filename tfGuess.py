import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from PIL import Image
X_test = np.load("X.npy")
y_test = np.load("Y.npy")
model = tf.keras.models.load_model('epic_num_reader.model')
predictions = model.predict([X_test])
nCorrect = 0
for i in range(len(predictions)):
    if np.argmax(predictions[i]) != y_test[i]:
        print("prediction: ", np.argmax(predictions[i]), "real: ", y_test[i])
        plt.imshow(X_test[i], cmap = plt.cm.binary)
        # print(predictions[i])
        plt.show()
    else:
        nCorrect += 1
print()
print(f"accuracy:  {nCorrect/len(predictions)*100}%")