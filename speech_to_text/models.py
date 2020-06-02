from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.
class Upload(models.Model):
    filename = models.CharField(max_length=100)
    uploaded_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=10)
    file_size = models.CharField(max_length=10)
    file_time = models.CharField(max_length=10)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.uploaded_name
