import streamlit as st
from PIL import Image

st.header('BMI CHECKER')

img=Image.open('R.jfif')
st.image(img.resize([500,350]))


w= st.number_input('Weight in Kg', step=0.1)
h= st.number_input('Height in meters')

def bmi_cal (w,h):
    bmi= w/(h**2)
    bmi = round(bmi,1)
    return (bmi)

def BMI_Status (bmi):

    if bmi < 18.5:
        return "You are at risk of beign underweight"
    
    elif 18.5 < bmi < 25:
        return "You are healthy"
    
    elif 24.9 < bmi < 30:
        return "Your are at risk of beign overweight"
    
    else:
        return "You are at risk of beign obese"
    

if st.button('Calculate'):  
    bmi = bmi_cal(w,h)
    status = BMI_Status(bmi)

    st.write(f'Your BMI is {bmi}')
    st. write(status)