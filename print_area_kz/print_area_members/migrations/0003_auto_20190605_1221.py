# Generated by Django 2.2.2 on 2019-06-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_area_members', '0002_auto_20190605_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='bin_code',
            field=models.IntegerField(verbose_name='БИН'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='checking_account',
            field=models.IntegerField(verbose_name='Расчетный счет'),
        ),
    ]