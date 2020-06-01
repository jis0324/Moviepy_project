import os
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .form import Upload_Form
from .models import Upload
from django.core.files.storage import FileSystemStorage
from django.conf import settings

FILE_TYPES = ['mp4', 'mp3', 'wav']

@login_required
def speech_upload(request):
  upload_form = Upload_Form()
  if request.method == "POST":
    uploaded_file = request.FILES['file']
    file_type = uploaded_file.name.split('.')[-1]
    file_type = file_type.lower()

    if file_type not in FILE_TYPES:
      return HttpResponse('wrong_type')
    
    location = settings.BASE_DIR + request.user.username + 'upload/'
    print(location)
    if not os.path.exists(location):
      os.makedirs(location)
      
    fs = FileSystemStorage(location = location)
    filename = fs.save(uploaded_file.name, uploaded_file)
    print(filename)
    uploaded_file_url = fs.url(filename)
    print(uploaded_file_url)
    return HttpResponse('success')
  # if request.method == "POST":
  #   upload_form = Upload_Form(request.POST, request.FILES)
  #   if upload_form.is_valid():
  #       uploaded_file = upload_form.save(commit=False)
  #       uploaded_file.file = request.FILES['file']
  #       file_type = uploaded_file.file.url.split('.')[-1]
  #       uploaded_file.file_type = file_type.lower()
  #       uploaded_file.user = request.user
  #       if file_type not in FILE_TYPES:
  #         return 'wrong_type'
  #       print(uploaded_file.file)
  #       uploaded_file.save()
  #       return 'success'

  context = {"form": upload_form,}
  return render(request, 'speech_to_text/upload.html', context)

def upload_audio(request):
  if request.method == "POST":
    print(request.POST)
    myfile = request.FILES['file']
    print(myfile)
    return HttpResponse('success')
