from django.db import models


# title = назване
# anons = анонс к статье, не обязателен
# content = основной текст статьи
# created_at = дата создания, сделать текущими в момент создания поста
# updated_at = дата редактирования, момент обновления
# photo = картинки к статьям, хранить в папке фото по дате
# published = натсраеваемая публикация. Если будет True, то статья опубликуется
class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    anons = models.CharField(max_length=250, blank=False)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    published = models.BooleanField(default=False, verbose_name='Статус')

    # возврат title в строковом выражении
    def __str__(self):
        return self.title

    # определить имена и сортировку по дате создания в обратном порядке
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
