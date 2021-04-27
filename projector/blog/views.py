from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm


# главная
# в переменной blog все поля модели Articles
def index(request):
    blog = Articles.objects.all()
    return render(request, 'blog/index.html', {'blog': blog})


# Опубликоввать статью
def public(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            Articles.objects.create(**form.cleaned_data)
    else:
        form = ArticlesForm()
    return render(request, 'blog/public.html', {'form': form})
