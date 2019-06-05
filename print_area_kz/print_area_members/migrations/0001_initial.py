# Generated by Django 2.2.2 on 2019-06-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=128, verbose_name='Юридическое наименование')),
                ('brand', models.CharField(max_length=128, verbose_name='Торговая марка')),
                ('logo', models.ImageField(upload_to='tenant/logo/<django.db.models.fields.CharField>', verbose_name='Логотип')),
                ('bin_code', models.PositiveIntegerField(verbose_name='БИН')),
                ('bank_props', models.CharField(choices=[('Каспи', 'Каспибанк'), ('Сбер', 'Сбербанк'), ('АТФ', 'АТФБанк'), ('ЕБ', 'Евразийский банк'), ('КН', 'Kassa Nova банк'), ('ВТБ', 'Банк ВТБ'), ('АК', 'AsiaCredit Bank'), ('ХК', 'ДБ Хоум Кредит энд Финанс Банк'), ('АБ', 'ДБ Альфа-Банк'), ('НБ', 'Нурбанк'), ('РБК', 'Bank RBK'), ('ФБ', 'ForteBank'), ('ЦК', 'Банк ЦентрКредит'), ('НБК', 'Народный Банк')], default='', max_length=7, verbose_name='Банк')),
                ('bank_bic', models.CharField(max_length=25, verbose_name='БИК')),
                ('checking_account', models.PositiveIntegerField(verbose_name='Расчетный счет')),
            ],
            options={
                'verbose_name': 'Тенант',
                'verbose_name_plural': 'Тенанты',
            },
        ),
    ]
