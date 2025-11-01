from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    """
    Модель для хранения информации о телефонах.
    """
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.URLField(verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(default=False, verbose_name='Поддержка LTE')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Автоматически генерирует slug при сохранении, если он не задан.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
