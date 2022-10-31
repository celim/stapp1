import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("My streamlit")

st.write("fantasic !!!")

st.sidebar.title("Side")
st.sidebar.radio("Select", ["A","B"])
st.sidebar.selectbox('Select Page',['Home','Prediction'])

st.camera_input("Camera")

# rand=np.random.normal(1, 2, size=20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)
# st.pyplot(fig)

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







    


