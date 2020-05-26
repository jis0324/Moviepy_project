from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'services/?$', views.services, name="services"),
    url(r'about/?$', views.about, name="about"),
    url(r'contact/?$', views.contact, name="contact"),
    # url(r'login/?$', views.handle_login, name='handle_login'),
]