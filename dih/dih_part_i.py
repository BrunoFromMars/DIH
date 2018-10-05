#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:49:09 2018

@author: jayesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('new.csv')

df['Month'] = pd.to_datetime(df['Month'])
index = df.iloc[146:,0:1]
index = np.reshape(index,(28,1))
index = pd.DataFrame(index)
index=index.reset_index()
index.drop(['index'], axis = 1, inplace = True)
df = df.set_index('Month')



split_date = '01-05-2016'
df = df[df.index>'01-05-2007']
train = df[df.index<split_date]
test = df[df.index>split_date]

plt.plot(train)
plt.plot(test)
plt.legend(['train','test'])



from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
train_sc = sc.fit_transform(train)
test_sc = sc.transform(test)

X_train = train_sc[:-1]
y_train = train_sc[1:]

X_test = test_sc[:-1]
y_test = test_sc[1:]

X_train = np.reshape(X_train,(107,1,1))
X_test = np.reshape(X_test,(28,1,1))



from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

model = Sequential()
model.add(LSTM(12,input_shape=(None,1),activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')
model.summary()
model.fit(X_train,y_train,epochs=200,batch_size=20,verbose=1)
y_pred = model.predict(X_test)


y_pred = sc.inverse_transform(y_pred)
y_test = pd.DataFrame(sc.inverse_transform(y_test))
import math
from sklearn.metrics import mean_squared_error
rmse = math.sqrt(mean_squared_error(y_test,y_pred))
rms = math.sqrt(mean_squared_error(np.zeros(28),y_test))





y_test = pd.DataFrame(y_test)
y_test['date']=index
y_pred = pd.DataFrame(y_pred)
y_pred=y_pred.iloc[1:,:]
y_pred=y_pred.reset_index()
y_pred.drop(['index'], axis = 1, inplace = True)
y_pred['date']=index
y_pred = y_pred.set_index('date')
y_test = y_test.set_index('date')

plt.plot(y_test)
plt.plot(y_pred)
plt.legend(['Actual Quantity','Predicted Quantity'])
plt.show()

import data_dict



dlt  = data_dict.dtm


print(getKeysByValue(dlt,'VERTIN 16MG TAB     15s'))
















