#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:15:20 2023

@author: zoz
"""
import pandas as pd
df=pd.read_csv('diabetes_prediction.csv')
print(df)
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
app=FastAPI()
class model_input(BaseModel):
     Pregnancies:int
     Glucose:int
     BloodPressure:int
     SkinThickness:int
     Insulin:int
     BMI:float
     DiabetesPedigreeFunction:float
     Age:int
       
       
diabetes_model=pickle.load(open('/home/zoz/Desktop/ML model as api/pythoncode/diabetes_model.sav','rb'))
@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    preg=input_dictionary['Pregnancies']
    glu=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dbf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
    input_list=[preg,glu,bp,skin,insulin,bmi,dbf,age]
    prediction=diabetes_model.predict([input_list])
    if (prediction[0]==0):
        print('The persion is not diabetic')
    else:            
        print('The person is diabetic')
        
    














    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
