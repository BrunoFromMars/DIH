#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:35:55 2018

@author: jayesh
"""

#importing the libraries and files

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import data_dict
import math
from sklearn.metrics import mean_squared_error




# importing actual data of diseases and medcines 
search_diseases = pd.read_csv('diseases.csv')
search_diseases['Month'] = pd.to_datetime(search_diseases['Month'])
search_diseases = search_diseases.set_index('Month')

search_medicine = pd.read_excel('list.xlsx')
search_medicine = search_medicine.set_index('Month')


#importing predicted data of diseases and medicines

predicted_diseases = pd.read_excel('predicted_diseases.xlsx')
predicted_diseases = predicted_diseases.set_index('Month')

predicted_medicines = pd.read_excel('predicted_medicines.xlsx')
predicted_medicines = predicted_medicines.set_index('Month')


# INput from user
disease = input("Enter a Disease: ")

# Checking whether the disease is in dataset or not to remove KeyError
while(disease not in data_dict.dtm.keys()):
    print("Sorry Data not available")
    disease = input("Enter a Disease: ")



#Extracting the list of medicines for the input disease bye the user

medicines = data_dict.dtm[disease] 



# Ploting the actual disease and the predicted diseasis from the dataset
plt.plot(search_diseases[disease])
plt.plot(predicted_diseases[disease])
plt.legend(['Actual value','Predicted value'])
plt.title([disease])
plt.xlabel(['Time'])


''' Looping through the list of medicines for plotting the graph of
     comparision between actual value and predicted value of the 
     medicines
     '''
for i in range(len(medicines)):
    
    #checking whether the medicine is the the predicted list or not
    
    if medicines[i] not in predicted_medicines.columns:
        continue
    
    #Calculating the RMSE of actual and predicted value
    medicine = pd.DataFrame(search_medicine[medicines[i]])
    predicted_medicines1 = predicted_medicines[medicines[i]]
    rmse = math.sqrt(mean_squared_error(predicted_medicines1,medicine[19:]))
    
    
    # Ploting the comparsion graoh of actual ; predicted; preicted + rmse;predicted-rmse
    plt.figure()
    plt.plot(medicine)
    plt.plot(predicted_medicines1)
    plt.plot(predicted_medicines1-rmse)
    plt.plot(predicted_medicines1+rmse)
    plt.title([medicines[i]])
    plt.xlabel(['Time'])
    plt.ylabel(['Quantity'])
    plt.legend(['Actual value','Predicted value','Minimum value','Maximum value'])
    plt.show()
    
