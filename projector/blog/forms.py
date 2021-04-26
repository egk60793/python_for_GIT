from django import forms
from .models import *

class ArticlesForm(forms.Form):
    title = forms.CharField(max_legth=150)
    anons = forms.CharField()
    content = forms.CharField()
    #photo
    published = forms.BoleanField()
    rubric = forms.ModelChoiseField(queryset=Category.objects.all)