import streamlit as st
st.title('Simple Calculator')

label = 'Enter first number'
num1 = st.number_input(label, min_value=None)

label2 = 'Enter second number'
num2 = st.number_input(label2, min_value=None)

add = st.button('ADD', key=None)
sub = st.button('SUBTRACT', key=None)
mul = st.button('MULTIPLY', key=None)
div = st.button('DIVIDE', key=None)

if add is True:
    res = num1 + num2
    st.subheader('Result - ' + str(res))
if sub is True:
    res = num1 - num2
    st.subheader('Result - ' + str(res))
if mul is True:
    res = num1*num2
    st.subheader('Result - ' + str(res))
if div is True:
    res = num1/num2
    st.subheader('Result - ' + str(res))