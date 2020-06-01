from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.
class Upload(models.Model):
    file= models.FileField(null=True, blank=True)
    file_type= models.CharField(max_length=10)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    result = models.TextField(null=True, blank=True)
    resulted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.file
