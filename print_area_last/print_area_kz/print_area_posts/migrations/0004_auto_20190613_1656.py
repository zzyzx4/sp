# Generated by Django 2.1.9 on 2019-06-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_area_posts', '0003_productimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImage',
            new_name='PostImage',
        ),
        migrations.AddField(
            model_name='post',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]
