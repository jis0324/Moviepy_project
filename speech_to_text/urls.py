from django.conf.urls import url
from . import views

app_name = 'speech_to_text'

urlpatterns = [
    url(r'^$', views.speech_upload, name="speech_to_text_upload"),
]