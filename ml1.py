# -*- coding: utf-8 -*-
"""ML1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AoSbM8Vn73DrDsoWqM8ZuGrZRPkDdViz
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as LR
import sys
print("Python version: ")
print(sys.version)
my_data = np.array([[4,100,10],[9,150,6],[15,200,17]])
my_column_names = ['Temperature','Quantity Available','Age']

mdf = pd.DataFrame(data=my_data, columns=my_column_names)

mdf.at[1, 'Temperature']
mdf['Price'] = [10,13,12]

mdf.index.name = "ID"

model = LR()
model.fit(mdf[['Temperature','Quantity Available','Age']],mdf['Price'])
print(model.intercept_.round(2))

x = 10
y = 160
z = 12
print(f"The model predicted the price to be "+str(model.predict([[x,y,z]])[0])+" based on the following inputs:\nTemperature = "+str(x)+"\nQuantity Available = "+str(y)+"\nAge = "+str(z))
mdf

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]
#target_words = ["document", "document", "one", "document"] # This was causing the error
# Instead of strings, use numerical labels for classification
target_labels = [0, 0, 1, 0, 2,2]  # Example: 0 for 'document', 1 for 'one'

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Train the logistic regression model # Changed to LogisticRegression
model = LR() # Changed to LogisticRegression
model.fit(X, target_labels)  # Use numerical labels

# Predict the target word for a new text
new_text = ["This is one one one one one one."]
X_new = vectorizer.transform(new_text)
predicted_label = model.predict(X_new)[0]  # Get predicted label
print(predicted_label)
# Map predicted label back to word (if needed)
label_to_word = {0: "document",1: "one"}  # Example mapping

predicted_word = label_to_word[predicted_label.round(0)]  # Get word from label

print(f"The predicted word is: {predicted_word}")



import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

df = pd.read_csv('test_scores.csv')
df['math']
x = [i for i in df['math']]
y = [i for i in df['cs']]
def gradient_descent(x,y):
  m_curr = b_curr = 0
  iterations = 100000
  n = len(x)
  learning_rate = 0.0002
  cost_previous = 0
  for i in range(iterations):

    y_predicted = [m_curr * val + b_curr for val in x]
    error = [val-val2 for val,val2 in zip(y,y_predicted)]
    cost = (1/n) * sum([val**2 for val in (error)])
    md = -(2/n)*sum(val1*val2 for val1,val2 in zip(x,error))
    bd = -(2/n)*sum(error)
    m_curr = m_curr - learning_rate * md
    b_curr = b_curr - learning_rate * bd
    print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

    if math.isclose(cost, cost_previous, rel_tol=1e-20):
            return m_curr, b_curr
            break
    cost_previous = cost


gradient_descent(x,y)

model = lm.LinearRegression().fit(df[['math']],df['cs'])
print(model.coef_)
print(model.intercept_)

import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt
from sklearn import linear_model as lm
from sklearn.model_selection import train_test_split as tts








df = pd.read_csv('sample_data/california_housing_test.csv')
medianprices = df['median_house_value']
df.drop('median_house_value',axis='columns',inplace=True)
price_test,price_train,variables_test,variables_train = tts(medianprices,df,test_size=0.2,random_state=10)
model = lm.LinearRegression().fit(variables_train,price_train)
dfff = model.predict(variables_test)
model.score(variables_test,price_test)

import pandas as pd
import keras as keras
from keras.models import Sequential as sequential
from keras.layers import Dense as dense
import tensorflow as tf
import numpy as np
import math as math
import matplotlib.pyplot as plt



(x_train,y_train) , (x_test,y_test) = keras.datasets.mnist.load_data(path="mnist.npz")
x_train = x_train / 255
x_test = x_test / 255
x_train_flattened = x_train.reshape(len(x_train),28*28)
x_test_flattened = x_test.reshape(len(x_test),28*28)

model = keras.Sequential([
    keras.layers.Dense(500,input_shape=(784,),activation='relu'),
    keras.layers.Dense(10,activation='sigmoid')
])
model.compile(
    optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train_flattened,y_train,epochs=5)
y_predicted = model.predict(x_test_flattened)
print("Predicted: "+ str(np.argmax(y_predicted[0])))
print("Actual Value: "+str(y_test[0]))
model.save('MNIST_digitTrained.keras')
print("Model has been saved successfully.")

model = keras.models.load_model('MNIST_digitTrained.keras')

import numpy as np
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

x_train = x_train/255
x_test = x_test/255

split_classes = [8,9]

mask_train_8 = np.isin(y_train,split_classes).flatten()
mask_test_8 = np.isin(y_test,split_classes).flatten()



x_train_8 , y_train_8 = x_train[mask_train_8],y_train[mask_train_8]
x_test_8 , y_test_8 = x_test[mask_test_8],y_test[mask_test_8]

mask_train_2 = np.isin(y_train,split_classes).flatten()
mask_test_2 = np.isin(y_test,split_classes).flatten()
x_train_2,y_train_2 = x_train[mask_train_2],y_train[mask_train_2]
x_test_2,y_test_2 = x_test[mask_test_2],y_test[mask_test_2]

y_train_2 = np.isin(y_train_2,split_classes[0]).astype(int)
y_test_2 = np.isin(y_test_2,split_classes[0]).astype(int)

model = Sequential(
  [
    Conv2D(32,(3,3),activation='relu',padding="same",input_shape=(32,32,3)),
    MaxPooling2D((2,2)),
    Dropout(0.25),

    Conv2D(64,(3,3),activation='relu',padding="same"),
    MaxPooling2D((2,2)),
    Dropout(0.25),

    Flatten(),
    Dense(512,activation='relu'),
    Dropout(0.5),
    Dense(10,activation='softmax')
  ]
)

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train_8,y_train_8,epochs=5,validation_data=(x_test_8,y_test_8))

model.layers[0].trainable= False
model.layers[1].trainable= False
model.layers[2].trainable= False
model.layers[3].trainable= False

model.pop()
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train_2,y_train_2,epochs=5,validation_data=(x_test_2,y_test_2))