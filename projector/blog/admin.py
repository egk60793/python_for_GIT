from django.contrib import admin
from .models import Articles



class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'published')

admin.site.register(Articles, ArticlesAdmin)