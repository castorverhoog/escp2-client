from PIL import Image
from numpy import asarray
import numpy as np


def loadbitmap(str = "./bitmaps/toad-small.png"):
  # load the image
  image = Image.open(str).rotate(90)
  # convert image to numpy array
  data = asarray(image)
  return_array = []
  # summarize shape
  for r in range(len(data)):
    return_array.append([])
    row = data[r]
    for c in range(len(row)):
      return_array[r].append(1 - round(np.mean(data[r][c])/255))
  return return_array
