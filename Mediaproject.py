from PIL import Image
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def get_size(image):
  return image.size

def quantization(image, n):
  return image.quantize(n)

def get_pixel_value(img,col,row):
  return img.getpixel((col,row))

def get_unique_values(image):
  return np.unique(image), len(np.unique(image))

def extract_row_color(arr,row,color):
  filtered = filter(lambda item: ((item[0] == row) and (item[-1] == color)), arr)
  return list(filtered)

def merge_row_color(filtered, row, color):
  remove_row_color = [item[1:-1] for item in filtered]
  merge_runs = (row,)
  for item in remove_row_color:
    merge_runs = merge_runs + item
  otp = merge_runs + (color,)
  return otp

image = Image.open('./tree.png')

#Task 1
def show_image_information(image):
  original_colors = []
  quantized_colors=[]
  # ......start code......
  original_colors, originalLength = get_unique_values(image)
  quantizedImage = quantization(image,9)
  quantized_colors, quantizedLength = get_unique_values(quantizedImage)
  # ......end code......
  return original_colors,quantized_colors

#Task 2
def compute_runs(image, unique_values):
  runs_code = []
  nRows = get_size(image)[1]
  nCols = get_size(image)[0]
  # ......start code......

  for i in range(nRows):
    row = i
    firstCol = 0
    prevColor = get_pixel_value(image, 0, i)
    for j in range(nCols):
      if(get_pixel_value(image,j,i)!=prevColor):
        runs_code.append((row,firstCol,(j-1),prevColor))
        firstCol=j
        prevColor = get_pixel_value(image, j, i)
    runs_code.append( (row,firstCol,(nCols-1), get_pixel_value(image, (nCols-1), i)))

  # ......end code......
  return runs_code


#Task 3
def compute_RLE(image, unique_values):
    result = []
    # ......start code......
    nRows = get_size(image)[1]
    arr = compute_runs(image, unique_values)
    for i in range(nRows):
      for c in unique_values:
        filtered = extract_row_color(arr, i, c)
        result.append(merge_row_color(filtered, i, c))
    # ......end code......
    return result

q = quantization(image,9)
original_colors,quantized_colors = show_image_information(image)
print(compute_RLE(q,quantized_colors))