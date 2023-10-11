from django import forms
from django.forms import ModelForm
from .models import *

class ActionForm(forms.ModelForm):
    
    class Meta:
        model = Action
        fields = ('action', 'about', 'deadline', 'done')