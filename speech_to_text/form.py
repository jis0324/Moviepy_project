from django import forms
from .models import Upload

#DataFlair
class Upload_Form(forms.ModelForm):
  class Meta:
    model = Upload
    fields = [
      'file'
    ]