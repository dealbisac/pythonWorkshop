import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://c.ndtvimg.com/2020-01/7inb8ce_python-generic_625x300_13_January_20.jpg")
print("Status Code", r.status_code)

image = Image.open(BytesIO(r.content))

path ="images."+image.format

print(image.size, image.format, image.mode)

#save the image
try:
    image.save(path, image.format)
except IOError:
    print("Cannot save the image.")