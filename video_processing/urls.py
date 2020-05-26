from django.conf.urls import url
from . import views

app_name = 'video_processing'

urlpatterns = [
    url(r'^$', views.video_tools),
    url(r'(?P<type>[\w\-]+)/upload?$', views.uploads, name="uploads"),
    url(r'upload_youtube/?$', views.upload_youtube_video, name="youtube_upload"),
]