from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def speech_upload(request):
  return render(request, 'speech_to_text/upload.html')
