import numpy as np

import io
from PIL import Image

# image test

import requests

url = 'http://localhost:8002'


# nd array로 표시
image_bytes = open('testimage.jpg','rb').read() 
print(image_bytes)
# image = np.array(Image.open(io.BytesIO(image_bytes))) 
# st.image(image)

# http
r = requests.get(f'{url}/image')
print(r.content)
# image = np.array(Image.open(io.BytesIO(r.content))) 
# st.image(image,channels = "RGB", output_format='JPEG')



