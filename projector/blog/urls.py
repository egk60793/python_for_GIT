from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('public/', public, name='public')
]