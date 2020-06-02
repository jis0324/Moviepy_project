import os
from datetime import datetime
import librosa
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Upload
from django.core.files.storage import FileSystemStorage
from django.conf import settings

FILE_TYPES = ['mp4', 'avi', 'mp3', 'wav']

def defalt_format(arg):
  if len(arg) == 1:
      arg = '0' + arg
  return arg

@login_required
def speech_upload(request):
  if request.method == "POST":
    try:
      uploaded_file = request.FILES['file']
      file_type = uploaded_file.name.split('.')[-1]
      file_type = file_type.lower()

      if len(uploaded_file.name) > 80:
        return HttpResponse('long_name')

      if file_type not in FILE_TYPES:
        return HttpResponse('wrong_type')
      
      location = settings.MEDIA_ROOT + '/speech-to-text/' + request.user.username + '/'
      file_name = str(datetime.now().year) + defalt_format(str(datetime.now().month)) + defalt_format(str(datetime.now().day)) + defalt_format(str(datetime.now().hour)) + defalt_format(str(datetime.now().minute)) + defalt_format(str(datetime.now().second)) + '-' + uploaded_file.name
      
      if not os.path.exists(location):
        os.makedirs(location)
      
      fs = FileSystemStorage(location = location)
      filename = fs.save(file_name, uploaded_file)
      file_size = os.stat(location + file_name).st_size
      file_play_time = librosa.get_duration(filename=location + file_name)
      uploaded_date = str(datetime.now().year) + '-' + defalt_format(str(datetime.now().month)) + '-' + defalt_format(str(datetime.now().day))
      upload_data = Upload( filename = uploaded_file.name, uploaded_name = file_name, file_type = file_type, file_size = file_size, file_time = file_play_time, uploaded_on = uploaded_date, status = 'uploaded', user = request.user)
      upload_data.save()
      return HttpResponse('success')
    except:
      return HttpResponse('error')
  return render(request, 'speech_to_text/upload.html', { 'page' : 'service' })

def lists(request):
  if request.method == "POST":
    print(request.POST)
    myfile = request.FILES['file']
    print(myfile)
    return HttpResponse('success')

  lists = Upload.objects.all()
  return render(request, 'speech_to_text/list.html', { 'lists' : lists, 'page' : 'service' })


