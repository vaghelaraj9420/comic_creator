from django import forms
from .models import ComicPanel

class ComicPanelForm(forms.ModelForm):
    class Meta:
        model = ComicPanel
        fields = ['text']
