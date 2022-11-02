import streamlit as st
import pandas as pd
import numpy as np
import time

# widgets

st.header("App2")

page = st.radio('Navigation', ['Checkbox','Button'])

st.write("**Page returns**", page)
if page == 'Checkbox' :
    # checkbox
    check = st.checkbox("Click here")
    st.write('state of the checkbox:', check)

    if check : 
        st.write(':smile:'*12)

else :
    st.write(':thumbsup::heart:')

    result = st.button('Say hello')
    st.write(result)

    if result:
        st.write('Why hello there')
    else:
        st.write('Goodbye')

# slider
x = st.slider('A number between 0..100', value=50)
st.write('Slider number',x)

y = st.slider('A number between 0..1', min_value=0.0, max_value=1.0, step=0.1)
st.write('Slider number',y)

# double slider
slider_range = st.slider("Double slider", value=[100,400], min_value=0,max_value=1000)
st.info("Type of slider_range is %s" % type(slider_range))
st.write('Slider range', slider_range, slider_range[0], slider_range[1])

# select_slider
temp_options = ['low', 'medium', 'high']
temp = st.select_slider('Choose temperature', options=temp_options)
st.write('The temperature is', temp)

# select box
st.subheader('select box')
selected = st.selectbox('Select Page',['Home','Prediction'])
st.write('Selected value is ', selected)

# np array
# st.subheader('select box with np array')
# array = np.array(([1,2,3], [4,5,6],[7,8,9]))

# col1, mid, col2 = st.columns([1,0.1,3])
# with col1 :
#     st.write('My array : ')
#     array

# array_selection = st.selectbox("Choose an option", options=array, index=1)

# st.write('Array selected is', array_selection, 'of type ', type(array_selection))
