from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import easyocr
import os


import numpy as np
import cv2
from PIL import ImageGrab, Image

# Create your views here.

def grabImageVid(request):
   
    leftTR = request.GET.get('leftTR', None)
    topTR = request.GET.get('topTR', None)
    widthTR = request.GET.get('widthTR', None)
    heightTR = request.GET.get('heightTR', None)
    image = ImageGrab.grab(bbox=(int(leftTR), int(topTR), int(widthTR), int(heightTR)))
    """
    path, dirs, files = next(os.walk("/home/zene/django-apps/yahw/blogs/image"))
    file_count = len(files) + 1
    name_files = "image__" + str(file_count) + "__.png"
    """

    imageUp = np.array(image)
    #cv2.imwrite("/home/zene/Desktop/image/" + name_files, imageUp)
    cv2.imwrite("./blogs/zenetare.png", imageUp)
  
    cv2.destroyAllWindows()
         
    reader = easyocr.Reader(['en'])
    #reader = easyocr.Reader(['en'])
    output = reader.readtext("./blogs/zenetare.png")
            
    if len(output) == 2 :
        valtran = output[0][1] + " " + output[1][1]
    elif len(output) == 3:
        valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]
    elif len(output) == 4:
        valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]
    elif len(output) == 5:
        valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]  + " " + output[4][1]
    elif len(output) == 6:
        valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]  + " " + output[4][1]  + " " + output[5][1]
    elif len(output) == 0:
            valtran = "undefine"
    else:
        valtran = output[0][1]
    
    zz= ""

    data = {
        "ti" : zz,
    }

    return JsonResponse(data)
     

def ajax(request):

    path, dirs, files = next(os.walk("/home/zene/Desktop/image"))
    file_count = len(files)
    path, dirs, files = next(os.walk("/home/zene/django-apps/yahw/blogs/text"))
    file_count_text = len(files) + 1

    for r in range(file_count) : 

         
        reader = easyocr.Reader(['en'], gpu=False)
        #reader = easyocr.Reader(['en'])
        output = reader.readtext("/home/zene/Desktop/image/image__" + str(r + 1) + "__.png")
            
        if len(output) == 2 :
            valtran = output[0][1] + " " + output[1][1]
        elif len(output) == 3:
            valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]
        elif len(output) == 4:
            valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]
        elif len(output) == 5:
            valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]  + " " + output[4][1]
        elif len(output) == 6:
            valtran = output[0][1] + " " + output[1][1] + " " + output[2][1]  + " " + output[3][1]  + " " + output[4][1]  + " " + output[5][1]
        elif len(output) == 0:
        	  valtran = "undefine"
        else:
            valtran = output[0][1]

        f = open("blogs/text/tran__" + str(r) + '__.text', "a")
        f.write(valtran)
        f.close()



     
    
    zz= ""

    data = {
        "ti" : zz,
    }

    return JsonResponse(data)


def tarn(request):
     
    """
    req = request.GET.get('countTran', None)
    f = open("blogs/text/tran__" + str(req) + "__.text", "r")
    rak = int(req) + 1
    """

    f = ""
    rak = int(1)
    data = {
        "ti" : f,
        "to" : rak
    }
    return JsonResponse(data)
    
    


