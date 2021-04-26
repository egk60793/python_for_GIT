from django import forms
from .models import *


class ArticlesForm(forms.Form):
    title = forms.CharField(max_length=150)
    anons = forms.CharField()
    content = forms.CharField()
    # photo
    published = forms.BooleanField()
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all())
