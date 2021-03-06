# Generated by Django 2.2.2 on 2019-06-24 07:37

import autoslug.fields
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'ordering': ['-title'],
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/%Y/%m/%d', verbose_name='картинки')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Посты',
                'ordering': ['-created_date'],
                'verbose_name': 'Пост',
            },
        ),
    ]
