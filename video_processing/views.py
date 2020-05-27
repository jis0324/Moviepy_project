from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def video_tools(request):
  return HttpResponse('video tools page!')

@login_required
def uploads(request, type):
  return render( request, 'tools/upload.html', { 'upload_type' : type} )

def upload_youtube_video(request):
  if request.method == "POST":
    print(request.POST['youtube_video_url'])
    print(request.POST['tool_type'])
    print('POST!')

  if request.method == "GET":
    print('GET!')