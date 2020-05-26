from django.shortcuts import render, HttpResponse

# Create your views here.

def video_tools(request):
  return HttpResponse('video tools page!')

def uploads(request, type):
  return render( request, 'tools/upload.html', { 'upload_type' : type} )

def upload_youtube_video(request):
  if request.method == "POST":
    print(request.POST['youtube_video_url'])
    print(request.POST['tool_type'])
    print('POST!')

  if request.method == "GET":
    print('GET!')