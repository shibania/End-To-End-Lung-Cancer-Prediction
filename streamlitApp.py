import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the model, scaler and encoder
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the input form for the user
st.title('Lung Cancer Prediction')
st.write('Please fill in the following details:')
Gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=15, max_value=100, step=1)
Smoking = st.selectbox('Smoking', ['Yes', 'No'])
Yellow_fingers = st.selectbox('Yellow fingers', ['Yes', 'No'])
Anxiety = st.selectbox('Anxiety', ['Yes', 'No'])
PEER_PRESSURE = st.selectbox('Peer Pressure', ['Yes', 'No'])
CHRONIC_DISEASE = st.selectbox('Chronic Disease', ['Yes', 'No'])
FATIGUE = st.selectbox('Fattigue', ['Yes', 'No'])
ALLERGY = st.selectbox('Allergy', ['Yes', 'No'])
WHEEZING = st.selectbox('Wheezing', ['Yes', 'No'])
ALCOHOL_CONSUMING = st.selectbox('Alcohol Consuming', ['Yes', 'No'])
COUGHING = st.selectbox('Coughing', ['Yes', 'No'])
SHORTNESS_OF_BREATH = st.selectbox('Shortness Of Breath', ['Yes', 'No'])
SWALLOWING_DIFFICULTY = st.selectbox('SWALLOWING DIFFICULTY', ['Yes','No'])
CHEST_PAIN = st.selectbox('CHEST_PAIN', ['Yes','No'])

# Encode the Gender feature
if Gender == 'Male':
    Gender = 1
else:
    Gender = 0

if Smoking == 'Yes':
    Smoking = 2
else:
    Smoking = 1

if Yellow_fingers == 'Yes':
    Yellow_fingers = 2
else:
    Yellow_fingers = 1

if Anxiety == 'Yes':
    Anxiety = 2
else:
    Anxiety = 1

if PEER_PRESSURE == 'Yes':
    PEER_PRESSURE = 2
else:
    PEER_PRESSURE = 1

if CHRONIC_DISEASE == 'Yes':
    CHRONIC_DISEASE = 2
else:
    CHRONIC_DISEASE = 1

if FATIGUE == 'Yes':
    FATIGUE = 2
else:
    FATIGUE = 1

if ALLERGY == 'Yes':
    ALLERGY = 2
else:
    ALLERGY = 1

if WHEEZING == 'Yes':
    WHEEZING = 2
else:
    WHEEZING = 1

if ALCOHOL_CONSUMING == 'Yes':
    ALCOHOL_CONSUMING = 2
else:
    ALCOHOL_CONSUMING = 1

if COUGHING == 'Yes':
    COUGHING = 2
else:
    COUGHING = 1

if SHORTNESS_OF_BREATH == 'Yes':
    SHORTNESS_OF_BREATH = 2
else:
    SHORTNESS_OF_BREATH = 1

if SWALLOWING_DIFFICULTY == 'Yes':
    SWALLOWING_DIFFICULTY = 2
else:
    SWALLOWING_DIFFICULTY = 1

if CHEST_PAIN == 'Yes':
    CHEST_PAIN = 2
else:
    CHEST_PAIN = 1

# Scale the input data
# input_data = pd.DataFrame({'Gender': [Gender],
#                            'age':[age],
#                            'Smoking': [Smoking],
#                            'Yellow_fingers': [Yellow_fingers],
#                            'Anxiety': [Anxiety],
#                            'PEER_PRESSURE': [PEER_PRESSURE],
#                            'CHRONIC_DISEASE': [CHRONIC_DISEASE],
#                            'FATIGUE': [FATIGUE],
#                            'ALLERGY': [ALLERGY],
#                            'WHEEZING' : [WHEEZING],
#                            'ALCOHOL_CONSUMING':[ALCOHOL_CONSUMING],
#                            'COUGHING':[COUGHING],
#                            'SHORTNESS_OF_BREATH':[SHORTNESS_OF_BREATH],
#                            'SWALLOWING_DIFFICULTY':[SWALLOWING_DIFFICULTY],
#                            'CHEST_PAIN':[CHEST_PAIN]})


input_data = [[Gender,age,Smoking,Yellow_fingers,Anxiety,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,
              ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]]
#input_data = input_data.reshape(-1,1)
input_data = np.array(input_data)

# input_data = input_data.reshape(-1,1)
# Make the prediction
prediction = model.predict(input_data)[0]

# Convert prediction to string output
if prediction == 1:
    result = 'The person is affected by lung cancer'
else:
    result = 'The person is not affected by lung cancer'

# Create submit button to display prediction
if st.button('Submit'):
    st.write(f'The predicted result is: {result}')