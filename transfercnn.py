# -*- coding: utf-8 -*-
"""TransferCNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Asx_K13rOmJ_0CV5VwXcm-HXSCz04AfR
"""

import keras
from tensorflow.keras import layers,models
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
import tensorflow as tf

conv_model = VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))
conv_model.trainable = False

conv_model.summary()

model = models.Sequential([
          conv_model,
          layers.Flatten(),
          layers.Dense(50,activation="relu"),
          layers.Dense(20,activation="relu"),
          layers.Dense(1,activation="sigmoid")
])
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

import zipfile
import os
import shutil
zipname = "train.zip"
with zipfile.ZipFile("/content/"+zipname,"r") as zipp:
    zipp.extractall("/content/extracted_files")



extracted_files_dir = "/content/extracted_files/"  # Directory containing all images

# Create the 'cat' and 'dog' subdirectories if they don't exist
os.makedirs(os.path.join("/content/extracted_files/", "cat"), exist_ok=True)
os.makedirs(os.path.join("/content/extracted_files/", "dog"), exist_ok=True)

# Iterate through files and move them to the appropriate folders
for filename in os.listdir(extracted_files_dir+zipname[:-4]):
    if filename.startswith("cat"):
        shutil.move(os.path.join(extracted_files_dir+zipname[:-4], filename),
                    os.path.join("/content/extracted_files/", "cat", filename))
    elif filename.startswith("dog"):
        shutil.move(os.path.join(extracted_files_dir+zipname[:-4], filename),
                    os.path.join("/content/extracted_files/", "dog", filename))
os.rmdir(extracted_files_dir+zipname[:-4])

import tensorflow as tf

extracted_files_dir = "/content/extracted_files"  # Directory containing extracted files

# Create a dataset from the images

dataset = tf.keras.utils.image_dataset_from_directory(
    extracted_files_dir,
    labels='inferred',  # Infer labels from subdirectory names
    label_mode='binary',  # Assuming you have two classes
    image_size=(224, 224),  # Resize images to this size
    interpolation='nearest',
    batch_size=32,  # Adjust as needed
    shuffle=True  # Shuffle the data
)

import tensorflow as tf
import matplotlib.pyplot as plt
imagesnp = []
labelsnp = []
class_names = ['Cat', 'Dog']
for images, labels in dataset:
    for image in images.numpy():
        imagesnp.append(image)
    for label in labels.numpy():
        labelsnp.append(label)

import numpy as np
imagesnp = np.array(imagesnp)/255

x_train = np.array(imagesnp[:1000])
y_train = np.array(labelsnp[:1000])

model.fit(x_train,y_train,batch_size=16,epochs=4)
model.save("transfermodel.keras")

error = 0
total = 1000
test_images = imagesnp[1000:2000]
test_labels = labelsnp[1000:2000]
print(test_images.shape)
y_pred = model.predict(test_images)

for i in range(0,1000):
 y_pred[i][0] = 0 if y_pred[i][0] < 0.5 else 1
 if y_pred[i][0] != test_labels[i]:
    plt.figure()
    plt.imshow(test_images[i])
    plt.show()

    error += 1

print(error/total)

test_images = test_images/255
test_labels = np.array(test_labels)
model.fit(test_images,test_labels,batch_size=32,epochs=3)