import streamlit as st

st.header('Lower Case to Upper Case')

st.write('Just for fun, click me')
btn1=st.button('click me ')    
if   btn1:
    st.balloons()
    st.image('Dhush1.jpg')    


x=st.text_input('Enter a string')

btn=st.button('click')
if btn:
    y=x.upper()
    st.subheader(y)
    st.balloons()




