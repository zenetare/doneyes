import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
from pylab import rcParams

reader = easyocr.Reader(['en'])
output = reader.readtext('zenetare.png')

print(output)
print(output[0][1])
print(output[1][1])
print(output[2][1])
print(len(output))