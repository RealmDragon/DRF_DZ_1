# Generated by Django 4.2 on 2024-07-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='телефон'),
        ),
    ]
