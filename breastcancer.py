# -*- coding: utf-8 -*-
"""BreastCancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Obi7uq9UNXGO2CB1V5DftgXbVVgWBCDg
"""

#Importing the Dependencies
import numpy as np#importing numpy for array operations
import pandas as pd#importing pandas for dataframe management
from sklearn.preprocessing import StandardScaler#for standerdizing the data
from sklearn.model_selection import train_test_split#for splitting the data into training and testing data
from sklearn import svm#support vector machine for classification 
from sklearn.metrics import accuracy_score#for calculating the accuracy percentage to determine how accurate the model is

cancer_data=pd.read_csv('/content/data.csv')

cancer_data.head()

cancer_data.drop(columns='id',axis=1,inplace=True)

cancer_data.head()

cancer_data.shape

cancer_data.isnull().sum()

cancer_data.drop(cancer_data.columns[-1],axis=1,inplace=True) 
#The last column is full of missing values and so we are dropping it

cancer_data.head()

X=cancer_data.drop(columns='diagnosis',axis=1)
Y=cancer_data['diagnosis']
print(X)
print(Y)

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

model=svm.SVC(kernel='linear')
model.fit(x_train,y_train)

predict1=model.predict(x_train)
predict2=model.predict(x_test)

score1=accuracy_score(predict1,y_train)
score2=accuracy_score(predict2,y_test)

print("Accuracy of Training Data Prediction ",score1)
print("Accuracy of Testing Data Prediction ",score2)

#Making a predictive system
input_data=(17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189)
#This is where we will be taking the input
input_data_as_numpy=np.asarray(input_data)#Transforming the input data into a array for ease of access
input_data_reshaped=input_data_as_numpy.reshape(1,-1)#reshaping the data
prediction=model.predict(input_data_reshaped)
print(prediction)

#Using a simple if and else systen to display the output
if(prediction[0]=='M'):
  print('Patient has Breast Cancer and needs further medical examination')

else:
  print('Patient does not have Breast Cancer')

