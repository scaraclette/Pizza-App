# Generated by Django 2.2.10 on 2020-03-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_pizza_isspecial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='totalTopping',
            field=models.IntegerField(default=0),
        ),
    ]
