import streamlit as st

import pickle as pkl

if 'data' not in st.session_state:
    st.session_state.data = {
        'age': 1,
        'weight': 1.0,
        'height': 0.1,
        'gender': 'Male',
        'frequency': 4,
        'type':'Cardio',
        'duration':1
    }

def calculate():
    data = st.session_state.data
    model = pkl.load(open('model.pkl','rb'))
    bmi = data['weight']/(data['height']**2)
    x_train = [[data['age'],data['gender'],data['duration']/60,data['type'],data['frequency'],bmi]]
    calories = int(model.predict(x_train)[0])
    st.success(f"✅ {calories} Calories Burnt!")

#UI---------------------------------------------------------------------------------------------------------
st.title("Calorie Burnt Tracker🔥")
st.subheader("Keep track of your fitness!")

data = st.session_state.data

age = st.number_input("Age",min_value=1,max_value=100,value=data['age'])
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight",min_value=1.0,max_value=300.0,step=0.1,value=data['weight'])
with col2:
    height = st.number_input("Height (in meter)",min_value=0.1,max_value=3.0,step=0.01,value=data['height'])

col3, col4 = st.columns(2)
with col3:
    gender = st.radio("Gender",["Male","Female"],index=["Male", "Female"].index(data['gender']))
with col4:
    frequency = st.slider("Workout Frequency (days/weak)",1,7,data['frequency'])

w1, w2 = st.columns(2)
with w1:
    type = st.selectbox("Workout Type",["Cardio", "Strength", "Yoga", "HIIT"],index=["Cardio", "Strength", "Yoga", "HIIT"].index(data['type']))


with w2:
    duration = st.number_input("Workout Duration (in minutes)",min_value=0,step=1,value=data['duration'])

st.markdown("""
    <style>
    div.stButton > button {
        font-size: 18px;
        padding: 10px 30px;
        background-color: #fe4b4a;
        color: white;
        border: none;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])  # Middle column is widest
with col2:
    if st.button("Calculate"):
        st.session_state.data = {
            'age': age,
            'weight': weight,
            'height': height,
            'gender': gender,
            'frequency': frequency,
            'type':type,
            'duration':duration
        }
        calculate()
