from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.conf import settings


class Post(models.Model):  # Посты
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Описание')
    place_name = models.TextField(null=True, blank=True, verbose_name='Название места')
    lng = models.DecimalField(max_digits=30, decimal_places=25, null=True, blank=True, verbose_name='Широта')
    lat = models.DecimalField(max_digits=30, decimal_places=25, null=True, blank=True, verbose_name='Долгота')

    date_upload = models.DateField(auto_now_add=True, verbose_name="Дата загрузки на сайт")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'a_id': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostGallery(models.Model):
    img = models.ImageField(null=True, verbose_name='Картинки поста', upload_to='posts/%Y/%m/%d')
    product = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class Account(models.Model):  # Профиль
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, verbose_name='Посты')
    avatar = models.ImageField(null=True, blank=True,
                               verbose_name='Картинка пользователя', upload_to='profiles/%Y/%m/%d')

    def __str__(self):
        return 'Профиль для {}'.format(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
