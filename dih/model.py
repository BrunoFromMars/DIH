#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 09:27:04 2018

@author: jayesh
"""

#____________________________________________________________________________________________________________________________
#importing libraries
import pandas as pd
import numpy as np
import math
import datetime
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
#____________________________________________________________________________________________________________________________
#importing data
data = pd.read_csv('diseases.csv')
split_date = datetime.datetime(2017, 11, 1)
data['Month']=pd.to_datetime(data['Month'])
pred_data = data['Month']
pred_data = pd.DataFrame(pred_data)
pred_data = pred_data[pred_data.Month > split_date]
pred_data= pred_data.iloc[1:,:].reset_index()
pred_data.drop(['index'], axis = 1, inplace = True)
data = data.set_index('Month')
m,n  = data.shape


for i in range(n):
#___________________________________________________________________________________________________________________________
#splitting data
    df = data.iloc[:,i:i+1]
    #split_date = datetime.datetime(2017, 11, 1)
    train = df[df.index < split_date]
    test = df[df.index > split_date]
#___________________________________________________________________________________________________________________________
#Scaling data
    sc = MinMaxScaler()
    train_sc = sc.fit_transform(train)
    test_sc = sc.transform(test)
    
    time_step = 1
    X_train = train_sc[:-time_step]
    y_train = train_sc[time_step:]

    X_test = test_sc[:-time_step]
    y_test = test_sc[time_step:]

    m,n = X_train.shape
    X_train = np.reshape(X_train,(m,n,1))
    m,n = X_test.shape
    X_test = np.reshape(X_test,(m,n,1))
#____________________________________________________________________________________________________________________________
#Training the model  
    model = Sequential()
    model.add(LSTM(12,input_shape=(None,1),activation='relu'))
    model.add(Dense(6))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error',optimizer='adam')
    model.summary()
    model.fit(X_train,y_train,epochs=80,batch_size=1,verbose=1)

    y_pred = model.predict(X_test)
    y_pred = sc.inverse_transform(y_pred)
    y = pd.DataFrame(sc.inverse_transform(y_test))
    
    y_pred = pd.DataFrame(y_pred)
    y_pred.columns = train.columns
#____________________________________________________________________________________________________________________________
# Calulating error
    rmse = math.sqrt(mean_squared_error(y,y_pred))

    pred_data = pred_data.join(y_pred)
    y_pred = y_pred.iloc[time_step:,:]
    y_pred = y_pred.reset_index()
    y_pred.drop(['index'], axis = 1, inplace = True)
    plt.plot(y)
    plt.plot(y_pred)
    
 
pred_data = pred_data.set_index('Month')
pred_data.to_excel('predicted_diseases.xlsx')
