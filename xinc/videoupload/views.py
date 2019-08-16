from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings

# Imaginary function to handle an uploaded file.
def uploadView(request):
    return render(request, "videoupload/index.html",{'media': settings.MEDIA_ROOT})

def upload_file(request):
    if request.method == 'POST':
        def handle_uploaded_file(f):
            with open(settings.MEDIA_ROOT+'/test.mp4', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        print("pause")
        handle_uploaded_file(request.FILES['test.mp4'])
        print("success")
    else:
        form = UploadFileForm()
    return render(request, "videoupload/index.html",{'media': settings.MEDIA_ROOT})