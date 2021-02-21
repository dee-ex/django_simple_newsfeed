from django import forms

from .models import SnewsfeedProfile

class SnewsfeedProfileForm(forms.ModelForm):
    class Meta:
        model = SnewsfeedProfile
        fields = ('avatar', )