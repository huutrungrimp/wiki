from django import forms
from .models import MyEntries
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class EntryForm(forms.ModelForm):
    class Meta:
        model = MyEntries
        fields = ['title', 'content']
