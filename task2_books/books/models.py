from django.db import models


class Book(models.Model):
    """
    Модель для хранения информации о книгах.
    """
    name = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=200, verbose_name='Автор')
    pub_date = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.name} - {self.author}'
