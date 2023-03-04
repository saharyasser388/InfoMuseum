from .models import *
from django import forms 

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['media', 'name']

