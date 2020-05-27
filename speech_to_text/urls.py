from django.conf.urls import url
from . import views

app_name = 'speech_to_text'

urlpatterns = [
    url(r'^$', views.speech_upload, name="speech_to_text_upload"),
    url(r'^upload/$', views.upload_audio, name="upload_texttospeech_file"),
]