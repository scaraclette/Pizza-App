# Generated by Django 2.2.10 on 2020-03-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_customersub_extracheese'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cartPaid',
            field=models.BooleanField(default=False),
        ),
    ]
