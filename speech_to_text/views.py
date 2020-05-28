from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def speech_upload(request):
  return render(request, 'speech_to_text/upload.html')

def upload_audio(request):
  if request.method == "POST":
    print(request.POST)
    myfile = request.FILES['file']
    print(myfile)
    return HttpResponse('success')
