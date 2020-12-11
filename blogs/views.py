from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import easyocr

import numpy as np
import cv2
from PIL import ImageGrab

# Create your views here.



def home(request):
    r = ''
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return redirect("/admin")


def new(request):
    r = ''
    if request.user.is_authenticated:
        return render(request, 'new.html', {})
    else:
        return redirect("/admin")


def ajax(request):
    leftTR = request.GET.get('leftTR', None)
    topTR = request.GET.get('topTR', None)
    widthTR = request.GET.get('widthTR', None)
    heightTR = request.GET.get('heightTR', None)
    image = ImageGrab.grab(bbox=(int(leftTR), int(topTR), int(widthTR), int(heightTR)))
    imageUp = np.array(image)
    cv2.imwrite("blogs/zenetare.png", imageUp)
    img = cv2.imread('blogs/zenetare.png', 0)
    cv2.imwrite("blogs/zenetare.png", img)
    cv2.destroyAllWindows()

    reader = easyocr.Reader(['en'])
    output = reader.readtext('blogs/zenetare.png')
    
    if len(output) == 2 :
        valtran = output[0][1]
    elif len(output) > 2 and len(output) < 6:
        valtran = output[0][1] + " " + output[1][1]
    else:
        valtran = output[0][1]
        pass

    
    data = {
        "ti" : valtran,
    }

    return JsonResponse(data)
