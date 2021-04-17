from django.contrib import admin
from .models import Articles, Rubric


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'published', 'rubric')
    list_display_links = ('id', 'title')
    list_editable = ('published',)

class RubricAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Rubric, RubricAdmin)