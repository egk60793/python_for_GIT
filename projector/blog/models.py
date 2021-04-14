from django.db import models

# title = назване
# anons = анонс к статье, не обязателен
# content = основной текст статьи
# created_at = дата создания, сделать текущими в момент создания поста
# updated_at = дата редактирования, момент обновления
# photo = картинки к статьям, хранить в папке фото по дате
# published = натсраеваемая публикация. Если будет True, то статья опубликуется

class Articles(models.Model):
    title = models.CharField(max_length=100)
    anons = models.CharField(max_length=250, blank=False)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    published = models.BooleanField(default=False)

    # возврат title в строковом выражении
    def __str__(self):
        return self.title
