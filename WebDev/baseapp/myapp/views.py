from django.shortcuts import render
from . import forms as F
from .models import Image

# Create your views here.

def home(request):
    return render(request, 'home.html')

def model(request):
    if request.method == "POST":
        context = F.ImgForm(request.POST, request.FILES)
        img = context.save()
        
        #This will be your classifaction
        result = None
        #--- YOUR MODEL HERE ---
        
        return render(request, 'model.html', {'context': context, 'img': img, 'result': result})
    else:
        context = F.ImgForm()
    return render(request, 'model.html', {'context': context})
