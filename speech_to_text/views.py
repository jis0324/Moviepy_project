import os
from datetime import datetime
import librosa
import time
import threading
import re
import shutil
import json
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Upload
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# speech to text import
import speech_recognition as sr
from tqdm import tqdm
import numpy as np
import scipy.io.wavfile as wavfile

AUDIO_TYPES = ['mp3', 'wav']
VIDEO_TYPES = ['mp4', 'avi']

def defalt_format(arg):
  if len(arg) == 1:
      arg = '0' + arg
  return arg

def make_key(arg):
  s = arg * 30
  key = time.strftime('%H:%M:%S', time.gmtime(s))
  return key


####################### speech to text ######################
# transcribe
def transcribe(file_name, username, id, file_type):
  wav_file_name = file_name[:-4] + '-w.wav'
  resulted_date = str(datetime.now().year) + '-' + defalt_format(str(datetime.now().month)) + '-' + defalt_format(str(datetime.now().day))
  location = settings.MEDIA_ROOT + '/speech-to-text/' + username + '/threading-' + str(threading.current_thread().ident) + '/'
  location1 = settings.MEDIA_ROOT + '/speech-to-text/' + username + '/threading-' + str(threading.current_thread().ident) + '-1/'
  i = 0
  while i < 5:
    i += 1
    try:
      
      file_exist = os.path.isfile(wav_file_name)
      if not file_exist:
        os.system('ffmpeg -y -threads 4 -i {} -f wav -ab 192000 -vn {}'.format(file_name, wav_file_name))
      
      data, srr = librosa.load(wav_file_name)
      duration = librosa.get_duration(data, srr)
      print('video duration : {}s'.format(duration))

      if os.path.exists(location):
        shutil.rmtree(location)
        os.makedirs(location)
      else:
        os.makedirs(location)
      for i in range(0,int(duration -1),30):
        tmp_batch = data[(i)*srr:srr*(i+30)]
        librosa.output.write_wav( location + '{}.wav'.format(chr(int(i/30)+65)), tmp_batch, srr)

      with open("s_to_t_secret.json") as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

      r = sr.Recognizer()
      files = sorted(os.listdir(location))

      result = dict()
      if os.path.exists(location1):
        shutil.rmtree(location1)
        os.makedirs(location1)
      else:
        os.makedirs(location1)

      for index, file in enumerate(tqdm(files)):
        name = location + file
        # Load audio file
        data, s = librosa.load(name)
        librosa.output.write_wav(location1 + 'tmp.wav', data, s)
        y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
        wavfile.write(location1 + 'tmp_32.wav', s, y)
        with sr.AudioFile(location1 + 'tmp_32.wav') as source:
            audio = r.record(source)
        try:
          text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
          key = make_key(index)
          result[key] = text
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
        except Exception as e:
            # print(e)
            continue

      os.remove(wav_file_name)
      shutil.rmtree(location)
      shutil.rmtree(location1)

      update_record = Upload.objects.get(id=id)
      update_record.result = json.dumps(result)
      update_record.status = 'Transcribed'
      update_record.resulted_on = resulted_date
      update_record.save()
      return
    except Exception as err:
      print(err)
      continue
  
  try:
    if os.path.isfile(os.path.isfile(wav_file_name)):
      os.remove(wav_file_name)
    if os.path.exists(location):
      shutil.rmtree(os.path.exists(location))
    if os.path.exists(location1):
      shutil.rmtree(os.path.exists(location1))

    update_record = Upload.objects.get(id=id)
    update_record.status = 'Failed'
    update_record.resulted_on = resulted_date
    update_record.save()
  except Exception as err:
    print(err)
    return
  


# upload
@login_required
def speech_upload(request):
  if request.method == "POST":
    try:
      lang = request.POST['lang']
      uploaded_file = request.FILES['file']
      file_extension = uploaded_file.name.split('.')[-1]
      file_extension = file_extension.lower()

      if len(uploaded_file.name) > 80:
        return HttpResponse('long_name')

      if file_extension in VIDEO_TYPES:
        file_type = 'video'
      elif file_extension in AUDIO_TYPES:
        file_type = 'audio'
      else:
        return HttpResponse('wrong_type')
      
      location = settings.MEDIA_ROOT + '/speech-to-text/' + request.user.username + '/'
      file_name = str(datetime.now().year) + defalt_format(str(datetime.now().month)) + defalt_format(str(datetime.now().day)) + defalt_format(str(datetime.now().hour)) + defalt_format(str(datetime.now().minute)) + defalt_format(str(datetime.now().second)) + '-' + re.sub(r'\s', '-', uploaded_file.name.strip())
      
      if not os.path.exists(location):
        os.makedirs(location)
      
      fs = FileSystemStorage(location = location)
      fs.save(file_name, uploaded_file)
      file_size = os.stat(location + file_name).st_size

      if file_size > 1000000000:
        file_size = "{:,.2f} GB".format(float(file_size / 1000000000))
      elif file_size > 1000000:
        file_size = "{:,.2f} MB".format(float(file_size / 1000000))
      elif file_size > 1000:
        file_size = "{:,.2f} KB".format(float(file_size / 1000))
      elif file_size > 0:
        file_size = "{:,.2f} B".format(float(file_size))
      else:
        file_size = 'Unkown'

      file_play_time = librosa.get_duration(filename=location + file_name)
      if file_play_time > 3600:
        formated_play_time = time.strftime('%Hh %Mm %Ss', time.gmtime(file_play_time))
      elif file_play_time > 60:
        formated_play_time = time.strftime('%Mm %Ss', time.gmtime(file_play_time))
      elif file_play_time > 0:
        formated_play_time = time.strftime('%Ss', time.gmtime(file_play_time))
      else:
        formated_play_time = "Unkown"

      uploaded_date = str(datetime.now().year) + '-' + defalt_format(str(datetime.now().month)) + '-' + defalt_format(str(datetime.now().day))
      upload_data = Upload( filename = uploaded_file.name, uploaded_name = file_name, file_type = file_type, file_size = file_size, file_time = formated_play_time, uploaded_on = uploaded_date, status = 'Uploaded', lang=lang, user = request.user)
      upload_data.save()

      # transcribing thread
      x = threading.Thread(target=transcribe, args=( location + file_name, request.user.username, upload_data.id, file_type))
      x.start()
      return HttpResponse('success')
    except Exception as err:
      print(err)
      file_exist = os.path.isfile(location + file_name)
      if file_exist:
        os.remove(location + file_name)
      return HttpResponse('error')
  return render(request, 'speech_to_text/upload.html', { 'page' : 'service' })

def lists(request):
  lists = Upload.objects.all()
  return render(request, 'speech_to_text/list.html', { 'lists' : lists, 'page' : 'service' })

def detail(request, id):
  record = Upload.objects.get(id=id)
  record.result = json.loads(record.result)
  return render(request, 'speech_to_text/detail.html', { 'detail' : record, 'page' : 'service'})
