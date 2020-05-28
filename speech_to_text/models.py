from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.
class Upload(models.Model):
    name= models.CharField(max_length=500)
    file= models.FileField(upload_to='videos/', null=True, verbose_name="")
    uploaded_on = models.DateTimeField(auto_now_add=True)
    result = models.TextField()
    resulted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ": " + str(self.videofile)
