from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


# главная
# в переменной blog все поля модели Articles
def index(request):
    blog = Articles.objects.all()
    return render(request, 'blog/index.html', {'blog': blog})


# Опубликоввать статью
def public(request):
    return render(request, 'blog/public.html')
