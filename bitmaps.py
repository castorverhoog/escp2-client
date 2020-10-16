from PIL import Image
from numpy import asarray

# load the image
image = Image.open("./bitmaps/toad.jpg")
# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)
for row in data:
  for cell in row:
    for val in cell:
      if(val != 0):
        cell = 1
      else:
        

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)