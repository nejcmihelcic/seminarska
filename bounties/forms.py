from django import forms

from .models import Bounty

class BountyForm(forms.ModelForm):
    class Meta:
        model=Bounty
        fields = ['name', 'text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}