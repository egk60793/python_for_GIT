from django import forms
from .models import *


class ArticlesForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'myClass'}))
    anons = forms.CharField(max_length=150, label='Анонос', required=False,
                            widget=forms.TextInput(attrs={'class': 'myClass'}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'myClass', 'rows': 5}))
    # photo
    published = forms.BooleanField(label='Опубликовать')
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Выбрать рубрику')
