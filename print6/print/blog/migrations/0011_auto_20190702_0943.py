# Generated by Django 2.2.2 on 2019-07-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190702_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='image',
            field=models.ImageField(default=1, upload_to='post/%Y/%m', verbose_name='фото'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SaleImage',
        ),
    ]
