from django import forms

from .models import Post, Response


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'category',
        ]
        labels = {
            'title': 'Заголовок',
            'body': '',
            'category': 'Категория',
        }


class ResponseCreateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'body',
        ]
        labels = {
            'body': ''
        }
