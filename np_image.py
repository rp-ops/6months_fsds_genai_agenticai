import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import requests
from io import BytesIO #bytes io used for buffer memory to store or capture images

def load_image_from_url(url):
    response=requests.get(url)
    return Image.open(BytesIO(response.content))

elephant_url="https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
#elephant_url="https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"
elephant=load_image_from_url(elephant_url)

# display an original image
# plt.figure(figsize=(6,10))
# plt.imshow(elephant)
# plt.title('Elephant')
# plt.axis('off')
# plt.show()

#image to array
elephant_np = np.array(elephant)
print('Elephant Image shape', elephant_np.shape)

#grayscale image
elephant_gray=elephant.convert('L')

plt.figure(figsize=(6,16))
plt.imshow(elephant_gray,cmap='cividis')
plt.title('Elephant(grayscale)')
plt.axis('off')
plt.show()


