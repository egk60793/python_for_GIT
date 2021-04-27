from django import forms
from .models import *


class ArticlesForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название статьи')
    anons = forms.CharField(max_length=500, label='Анонс статьи')
    content = forms.CharField(label='Основной контент', widget=forms.Textarea)
    # photo
    published = forms.BooleanField(label='Опубликовать сразу')
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Выбрать рубрику')
