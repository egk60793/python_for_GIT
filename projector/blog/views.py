from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


# в переменной blog все поля модели Articles
def index(request):
    blog = Articles.objects.all()
    return render(request, 'blog/index.html', {'blog': blog, 'test': 'testik'})