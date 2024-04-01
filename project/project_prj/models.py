from django.db import models
from django.core.validators import FileExtensionValidator


class Task(models.Model):
    name = models.CharField('Название товара', max_length=100)
    place = models.CharField('Объём', max_length=100, )
    price = models.IntegerField('Цена')
    square = models.IntegerField('Количество')
    thumbnail = models.ImageField(
        verbose_name='Превью поста',
        blank=True,
        upload_to='images/thumbnails/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Orders(models.Model):
    created = models.DateTimeField(verbose_name='Дата')
    owner = models.ForeignKey('auth.User', verbose_name='Автор', related_name='orders_user',
                              on_delete=models.CASCADE)
    task = models.ForeignKey('Task', verbose_name='Услуга', related_name='orders_task', on_delete=models.CASCADE)
    phone = models.CharField('Телефон', max_length=16)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.created)

    def get_absolute_url(self):
        return "/orders/%s" % self.owner.username
        # return "/orders/%i/" % self.id

    class Meta:
        ordering = ['created']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class FileExtensionValidator:
    pass
