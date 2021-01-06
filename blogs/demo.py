import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
from pylab import rcParams

reader = easyocr.Reader(['en'])
output = reader.readtext('zenetare2.png')
"""
print(len(output))
print(output)

print('___________')

print(output[0])



print('___________')

print(output[1])
"""
if len(output) == 2 :
    valtran = output[0][1] + " " + output[1][1] + " 1"
elif len(output) == 3:
    valtran = output[0][1] + " " + output[1][1] + " " + output[2][1] + " 2"
elif len(output) == 4:
    valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1] + " 3"
elif len(output) == 5:
    valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]  + " " + output[4][1] + " 4"
elif len(output) == 6:
    valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]  + " " + output[4][1]  + " " + output[5][1]
else:
    valtran = output[0][1] + " 5"

print(output)
print(valtran)