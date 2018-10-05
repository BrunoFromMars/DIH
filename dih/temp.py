import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

'''
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size =0.25, random_state 0) 




#FEature Scalling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Fitting random forest Classicfication

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators =10, criterion = 'entropy', random_state =0)
classifier.fit(X_train,y_train)

#Predicting the TEst set results

'''

# importing necessary libraries

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
 
seed = 7


dataset_x = pd.read_excel('Product List_ws.xlsx')
dataset_y = pd.read_csv('DIH.csv')
 



'''
# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
 
'''


# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(8, input_dim=4, activation='relu'))
	model.add(Dense(3, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)


kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, dataset_x, dataset_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))




'''

# training a DescisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)
 
# creating a confusion matrix
cm = confusion_matrix(y_test, dtree_predictions)

'''
