# Generated by Django 2.2.2 on 2019-06-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
