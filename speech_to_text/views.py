from django.shortcuts import render, HttpResponse

def speech_upload(request):
  return render(request, 'speech_to_text/upload.html')
