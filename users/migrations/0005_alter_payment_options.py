# Generated by Django 4.2 on 2024-07-19 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_payments_payment_alter_payment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ('-payment',), 'verbose_name': 'платеж', 'verbose_name_plural': 'платежи'},
        ),
    ]
