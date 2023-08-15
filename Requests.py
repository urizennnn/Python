import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)


print(r.request.headers)
print(r.status_code)
print("request body:", r.request.body)
header=r.headers
print(r.headers)
print(header['date'])
print(header['Content-type'])
print(r.encoding)