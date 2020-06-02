import os
from datetime import datetime
import librosa
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Upload
from django.core.files.storage import FileSystemStorage
from django.conf import settings

FILE_TYPES = ['mp4', 'mp3', 'wav']

@login_required
def speech_upload(request):
  if request.method == "POST":
    uploaded_file = request.FILES['file']
    file_type = uploaded_file.name.split('.')[-1]
    file_type = file_type.lower()

    if file_type not in FILE_TYPES:
      return HttpResponse('wrong_type')
    
    location = settings.MEDIA_ROOT + '/speech-to-text/' + request.user.username + '/'
    if not os.path.exists(location):
      os.makedirs(location)
      
    fs = FileSystemStorage(location = location)
    file_name = str(datetime.now().year) + defalt_format(str(datetime.now().month)) + defalt_format(str(datetime.now().day)) + defalt_format(str(datetime.now().hour)) + defalt_format(str(datetime.now().minute)) + defalt_format(str(datetime.now().second)) + '-' + uploaded_file.name
    filename = fs.save(file_name, uploaded_file)
    file_size = os.stat(location + file_name).st_size
    file_play_time = librosa.get_duration(filename=location + file_name)
    upload_data = Upload( filename = uploaded_file.name, uploaded_file = file_name, file_type = file_type, file_size = file_size, file_time = file_play_time, user = request.user)
    upload_data.save()
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

  return render(request, 'speech_to_text/upload.html')

def upload_audio(request):
  if request.method == "POST":
    print(request.POST)
    myfile = request.FILES['file']
    print(myfile)
    return HttpResponse('success')

def defalt_format(arg):
  if len(arg) == 1:
      arg = '0' + arg
  return arg
