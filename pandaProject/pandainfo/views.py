from django.shortcuts import render,redirect,HttpResponse
from pandainfo.forms import UploadFileForm
from django.http import Http404
from .models import Upload
from django.conf import settings

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

# Create your views here.

def ModelFormUpload(request):
    if request.POST:
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'pandainfo/info.html')
    else:
        form = UploadFileForm()

        return render(request, 'pandainfo/upload.html', {'form': form})

#####



def info(request):
    allimages = Upload.objects.all()
    return render(request,"pandainfo/info.html",{"images":allimages})
