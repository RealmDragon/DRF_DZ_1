# Generated by Django 4.2 on 2024-10-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_payment_link_payment_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата платежа'),
        ),
    ]