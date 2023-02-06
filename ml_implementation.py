#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:30:54 2023

@author: zoz
"""

import json 
import requests
url='http://127.0.0.1:8000'
input_data_for_model={
    
    'Pregnancies':6,
    'Glucose':148,
    'BloodPressure':72,
    'SkinThickness':35,
    'Insulin':0,
    'BMI':33.6,
    'DiabetesPedigreeFunction':0.627,
    'Age':50
    
    }
input_json=json.dumps(input_data_for_model)
response=requests.post(url,data=input_json)
print(response.text)