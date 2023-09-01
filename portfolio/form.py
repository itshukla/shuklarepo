from django import forms
from .models import *

class userForm(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'