from django import forms

from .models import Post, DatePost


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('number','date','type','amount')

class DateForm(forms.ModelForm):
    class Meta:
        model=DatePost
        fields=('number','date','amount')
