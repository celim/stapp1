import streamlit as st
import pandas as pd
import numpy as np
import time

# getting started
# https://celim-stapp1-app-fsvmgy.streamlitapp.com/


st.title("My streamlit")

st.write("fantasic !!!")

st.sidebar.title("Side")
st.sidebar.radio("Select", ["A","B"])
st.sidebar.selectbox('Select Page',['Home','Prediction'])

st.camera_input("Camera")

# image
st.subheader("Image")

# file 표시
st.image('testimage.jpg',caption='display with file')

# http
url = 'http://localhost:8002'
r = requests.get(f'{url}/image')
print(r.content)
image = np.array(Image.open(io.BytesIO(r.content))) 
st.image(image,caption='display with httpget')

# 
st.subheader("Dataframe")
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)
st.bar_chart(df)

btn = st.button("Press for progress")

if btn:
    progrss = st.progress(0)

    with st.spinner('Wait for it...'):
        for i in range(10):
            # print(i)
            progrss.progress((i+1) * 10)
            time.sleep(0.1)
        

st.info("Done")







    


