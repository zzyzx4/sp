# Generated by Django 2.2.1 on 2019-05-24 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('public_area', '0006_product_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Город'),
            preserve_default=False,
        ),
    ]
