# -*- coding: utf-8 -*-
"""sem_res.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tpJWX42ZX9BSi8fHe3cUHgwiJ3wWPGMA
"""

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

Dataset = pd.read_csv('sem_res.csv')

Dataset.head()

X = Dataset.drop(columns=['%'])
y = Dataset[['%']]
X.head()

y.head()

def baseline_model():
  model = Sequential()
  model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu',input_shape=[None, None, 2]))
  model.add(Dense(1, kernel_initializer='normal'))
  # Compile model
  model.compile(loss='mean_squared_error', optimizer='adam',metrics=['mean_squared_error'])
  print('----Model Successfully Compiled----')
  return model

mymodel = baseline_model()
mymodel.summary()



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=5) 
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
history = mymodel.fit(X_train, y_train,
                  batch_size = 10,
                  epochs = 100, 
                  validation_data = (X_test, y_test),
                  verbose=1)

score = mymodel.evaluate(X,y)

score = score[1]
print("The mean squared error is ",score)