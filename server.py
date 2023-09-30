import pickle
import numpy as np
import streamlit as st

MODEL_FILE_NAME = "model.pk"

def load_model():
    print("Loading the model...")
    with open('./models/' + MODEL_FILE_NAME, 'rb') as f:
        model = pickle.load(f)
        print("The model has been loaded...doing predictions now...")
        return model
    
model = load_model()

st.header("Игра в жизнь.")
st.write("Запишите все данные, чтобы узнать результат!")

age = st.number_input('Age of the person')
sex = st.radio("Gender of the person. 0: Women moment. 1: Male", [0, 1])
cp = st.radio('Chest Pain type chest pain type. 1: typical angina. 2: atypical angina. 3: non-anginal pain. 4: asymptomatic',
              [1, 2, 3, 4])
trtbps = st.number_input('Resting blood pressure (in mm Hg)')
chol = st.number_input('Cholestoral in mg/dl fetched via BMI sensor')
fbs = st.radio("Fasting blood sugar > 120 mg/d? 1: True. 2. False",
               [0, 1])
restecg = st.radio("Resting electrocardiographic results."\
    + "0: normal. 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)"\
    + "2: showing probable or definite left ventricular hypertrophy by Estes' criteria",
    [0, 1, 2])
thalachh = st.number_input('Maximum heart rate achieved')
exng = st.radio("Exercise induced angina (1 = yes; 0 = no)", [0, 1])
oldpeak = st.number_input('ST depression induced by exercise relative to rest')
slp = st.radio('The slope of the peak exercise ST segment. 0: upsloping. 1: flat. 2: downsloping.', [0, 1, 2])
caa = st.number_input('Number of major vessels (0-3)')
thall = st.radio('Thal: 1 = normal; 2 = fixed defect; 3 = reversable defect', [1, 2, 3])

params = [age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]

if st.button('Результат') and not None in params:
    result = model.predict([params])
    st.write(result)
    if (result == 1):
        st.header("ПОМЕР", divider="red")
    else:
        st.header("ЖИТЬ ЖИТЬ ЖИТЬ", divider="green")
        

st.button("Убрать все нахуй", type="primary")