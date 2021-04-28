from django import forms
from .models import *


# class ArticlesForm(forms.Form):
#    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'myClass'}))
#    anons = forms.CharField(max_length=150, label='Анонос', required=False,
#                            widget=forms.TextInput(attrs={'class': 'myClass'}))
#    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'myClass', 'rows': 5}))
#    # photo
#    published = forms.BooleanField(label='Опубликовать')
#    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Выбрать рубрику',
#                                    widget=forms.Select(attrs={'class': 'myClass'}))


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'published', 'rubric']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'myClass'}),
            'anons': forms.TextInput(attrs={'class': 'myClass'}),
            'content': forms.Textarea(attrs={'class': 'myClass', 'rows': 5}),
            'rubric': forms.Select(attrs={'class': 'myClass'})
        }