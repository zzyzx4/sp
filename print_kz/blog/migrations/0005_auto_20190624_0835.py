# Generated by Django 2.2.2 on 2019-06-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='post/%Y/%m/%d', verbose_name='картинки'),
            preserve_default=False,
        ),
    ]
