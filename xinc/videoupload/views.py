from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NameForm
from django.conf import settings
from .models import Video


#debug
import shutil
import os

# Imaginary function to handle an uploaded file.
def uploadView(request):
    return render(request, "videoupload/better.html",{'media': settings.MEDIA_ROOT, 'form': NameForm()})

def upload_file(request):
    if request.method == 'POST':
        def handle_uploaded_file(f):
            with open(settings.MEDIA_ROOT+'/test.mp4', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        print("pause")
        handle_uploaded_file(request.FILES['test.mp4'])
        print("success")
    form = NameForm()
    return render(request, "videoupload/index.html",{'media': settings.MEDIA_ROOT, 'form': NameForm()})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with data from the
            #request
        form = NameForm(request.POST)
        #check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data
            #redirect to better SUCCESS URL
            return HttpResponseRedirect('/thanks/')
        else:
            #GET request will create an empty form instance
                #and place it in a template context to be rendered
            print("HERE!")
            form = NameForm()
            return render(request, 'videoupload/name.html', {'form' : form})

def file_list(request):
    return render(request, "videoupload/videolist.html",
                      {'story_list': Video.objects.all()})

def watch_video(request, name):
    return render(request, "videoupload/watch.html", {'name' : name})


#JUST FOR DEBUGING, DO NOT TRAVERSE TO THIS LINK UNLESS YOU WANT TO CLEAR DB
def clear_database(request):
    Video.objects.all().delete()
    #clearing videos on server too
    shutil.rmtree(settings.MEDIA_ROOT)
    os.mkdir(settings.MEDIA_ROOT)
    return redirect("/polls/filelist/")

def write_file(request):
    def handle_uploaded_file(f, name):
        with open(settings.MEDIA_ROOT + name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    #check if the video is unique
    def check_unique(name):
        try:
            return Video.objects.get(name=name)
        except:
            return False

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with data from the
            #request
        form = NameForm(request.POST)
        #check whether it's valid
        if form.is_valid():
            if not check_unique(form.cleaned_data['file_name']):
                handle_uploaded_file(request.FILES['test.mp4'],
                                     form.cleaned_data['file_name'])
                temp = Video.objects.create(name=form.cleaned_data['file_name'])
                temp.save()

        return redirect("/polls/filelist/")
