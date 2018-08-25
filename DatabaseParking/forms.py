from django import forms

from .models import Post, DatePost


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('number','date')

class DateForm(forms.ModelForm):
    class Meta:
        model=DatePost
        fields=('date','type','amount')
