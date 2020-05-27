from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name')

    # def save(self, commit=True):
    #     user = super(CustomUserCreationForm, self).save(commit=False)
    #     user.first_name = cleaned_data['first_name']
    #     user.last_name = cleaned_data['last_name']
    #     user.email = cleaned_data['email']

    #     if commit:
    #         user.save()
        
    #     return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields