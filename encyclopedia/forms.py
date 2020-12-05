from django import forms
from .models import MyEntries
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class EntryForm(forms.ModelForm):
    class Meta:
        model = MyEntries
        fields = ['title', 'content']

    '''def clean_title(self):
        title = self.cleaned_data.get('title')
        for instance in MyEntries.objects.all():
            if instance.title == title:
                raise forms.ValidationError('The title already exists. Do you still want to save')

        return title'''