from django.conf.urls import url
from . import views

app_name = 'speech_to_text'

urlpatterns = [
    url(r'^upload/$', views.speech_upload, name="speech_to_text_upload"),
    url(r'^list/$', views.lists, name="speech_to_text_lists"),
]