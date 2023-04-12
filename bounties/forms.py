from django import forms

from .models import Bounty, Comment

class BountyForm(forms.ModelForm):
    class Meta:
        model=Bounty
        fields = ['name', 'text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}