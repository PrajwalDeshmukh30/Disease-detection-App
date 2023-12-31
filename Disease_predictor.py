# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:37:05 2023

@author: PRAJWAL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu as om

diabetes_model = pickle.load(open("C:/Users/PRAJWAL/Documents/Disease Prediction Project/Diabetes_model.sav", 'rb'))
parkinsons_model = pickle.load((open("C:/Users/PRAJWAL\Documents/Disease Prediction Project/Parkinson_model.sav", 'rb')))
breast_cancer_model = pickle.load(open("C:/Users/PRAJWAL/Documents/Disease Prediction Project/Breast_Cancer_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = om('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Breast Cancer Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        clump_thickness = st.text_input('Clump Thickness')
        
    with col2:
        cell_size = st.text_input('cell_size')
        
    with col3:
        cell_shape = st.text_input('Cell Shape')
        
    with col1:
        marginal_adhesion = st.text_input('marginal Adhesion')
        
    with col2:
        se_cell_size = st.text_input('SE cell Size')
        
    with col3:
        bare_nuclei = st.text_input('bare nuclei')
        
    with col1:
        bland_chromatin = st.text_input('Bland Chromatin')
        
    with col2:
        normal_nucleoli = st.text_input('Normal Nucleoli')
        
    with col3:
        mitosis = st.text_input('Mitosis')
        
   
        
        
     
     
    # code for Prediction
    cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast cancer Test Result'):
        cancer_prediction = breast_cancer_model.predict([[clump_thickness, cell_size, cell_shape, marginal_adhesion, se_cell_size, bare_nuclei, bland_chromatin, normal_nucleoli, mitosis]])                          
        
        if (cancer_prediction[0] == 1):
          cancer_diagnosis = 'The person is having breast cancer'
        else:
          cancer_diagnosis = 'The person does not have breast cancer'
        
    st.success(cancer_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

