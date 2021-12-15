from django.db import models
from django.urls import reverse
from PIL import Image
from django.conf import settings


class Account(models.Model):  # Профиль
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True,
                               verbose_name='Картинка пользователя', upload_to='profiles/%Y/%m/%d')

    def __str__(self):
        return 'Профиль для {}'.format(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class PostGallery(models.Model):
    img = models.ImageField(null=True, blank=True, verbose_name='Картинка поста', upload_to='posts/%Y/%m/%d')

    def save(self, *args, **kwargs):
        super().save()
        if self.img:
            image = Image.open(self.img.path)
            if image.height > 200 or image.width > 400:
                output_size = (400, 400)
                image.thumbnail(output_size)
                image.save(self.img.path)

    class Meta:
        verbose_name = 'Картинка поста'
        verbose_name_plural = 'Картинки поста'


class Post(models.Model):  # Посты
    author = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, verbose_name='Автор поста')
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Описание')
    gallery = models.ManyToManyField(PostGallery, verbose_name="Картинки поста")
    date_upload = models.DateField(auto_now_add=True, verbose_name="Дата загрузки на сайт")
    lat = models.FloatField(blank=True, null=True, verbose_name="Широта")
    lon = models.FloatField(blank=True, null=True, verbose_name="Долгота")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'a_id': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
