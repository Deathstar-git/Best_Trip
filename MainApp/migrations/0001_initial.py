# Generated by Django 3.2.8 on 2021-12-11 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('lng', models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='Широта')),
                ('lat', models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='Долгота')),
                ('date_upload', models.DateField(auto_now_add=True, verbose_name='Дата загрузки на сайт')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='PostGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='posts/%Y/%m/%d', verbose_name='Картинки поста')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='MainApp.post')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d', verbose_name='Картинка пользователя')),
                ('posts', models.ManyToManyField(to='MainApp.Post', verbose_name='Посты')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
