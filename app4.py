import streamlit as st
import pandas as pd
import numpy as np
import time
import io
from PIL import Image

# image test

import requests



st.header('Image')

# file 표시
st.image('testimage.jpg',caption='display with file')

# nd array로 표시
image_bytes = open('testimage.jpg','rb').read() 
image = np.array(Image.open(io.BytesIO(image_bytes))) 
st.image(image,caption='display with ndarray')

# http
url = 'http://localhost:8002'
r = requests.get(f'{url}/image')
print(r.content)
image = np.array(Image.open(io.BytesIO(r.content))) 
st.image(image,caption='display with httpget')




