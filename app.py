# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# cargando los modelos guardados

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# barra lateral para navegación
with st.sidebar:
    
    selected = option_menu('Sistema de Predicción de Enfermedades Múltiples - UTP',
                          
                          ['Predicción de diabetes',
                           'Predicción de enfermedades del corazón',
                           'Predicción de Parkinson'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Página de predicción de diabetes
if (selected == 'Predicción de diabetes'):
    
# Título de la página
    st.title('Predicción de diabetes - UTP')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Número de embarazos')
        
    with col2:
        Glucose = st.text_input('Nivel de glucosa')
    
    with col3:
        BloodPressure = st.text_input('Valor de la presión arterial')
    
    with col1:
        SkinThickness = st.text_input('Valor del grosor de la piel')
    
    with col2:
        Insulin = st.text_input('Nivel de insulina')
    
    with col3:
        BMI = st.text_input('valor del IMC')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Valor de función de pedigrí de diabetes')
    
    with col2:
        Age = st.text_input('Edad de la persona')
    
    
    diab_diagnosis = ''
    
    # Creacion de boton de prediccion
    
    if st.button('Resultado de la prueba'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'La persona es diabética'
        else:
          diab_diagnosis = 'La persona no es diabética'
        
    st.success(diab_diagnosis)




# Página de predicción de enfermedades del corazón
if (selected == 'Predicción de enfermedades del corazón'):
    

# Título de la página
    st.title('Predicción de enfermedades cardíacas ')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Años')
        
    with col2:
        sex = st.text_input('Sexo')
        
    with col3:
        cp = st.text_input('Tipos de dolor de pecho')
        
    with col1:
        trestbps = st.text_input('Presión arterial en reposo')
        
    with col2:
        chol = st.text_input('Colesterol sérico en mg/dl')
        
    with col3:
        fbs = st.text_input('Azúcar en sangre en ayunas > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resultados electrocardiográficos en reposo')
        
    with col2:
        thalach = st.text_input('Frecuencia cardíaca máxima alcanzada')
        
    with col3:
        exang = st.text_input('Angina inducida por ejercicio')
        
    with col1:
        oldpeak = st.text_input('Depresión del ST inducida por el ejercicio')
        
    with col2:
        slope = st.text_input('Pendiente del segmento ST de ejercicio máximo')
        
    with col3:
        ca = st.text_input('Grandes vasos coloreados por fluoroscopia')
        
    with col1:
        thal = st.text_input('tal: 0 = normal; 1 = defecto fijo; 2 = defecto reversible')
        
        
     
     
# código para Predicción
    heart_diagnosis = ''
    
  # creando un botón para Predicción
    
    if st.button('Resultado de la prueba'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'La persona tiene una enfermedad cardíaca.'
        else:
          heart_diagnosis = 'La persona no tiene ninguna enfermedad del corazón.'
        
    st.success(heart_diagnosis)
        
    
    

# Página de predicción de Parkinson
if (selected == "Predicción de Parkinson"):
    
    # page title
    st.title("Predicción de la enfermedad de Parkinson")
    
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
        
    
    
# código para Predicción
    parkinsons_diagnosis = ''
    
# creando un botón para Predicción
    if st.button("Resultado de la prueba de Parkinson"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "La persona tiene la enfermedad de Parkinson."
        else:
          parkinsons_diagnosis = "La persona no tiene la enfermedad de Parkinson."
        
    st.success(parkinsons_diagnosis)
















