# Generated by Django 2.2.10 on 2020-03-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200317_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]