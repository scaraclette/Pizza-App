# Generated by Django 2.2.10 on 2020-03-16 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200315_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='pizzaOrdered',
            field=models.ManyToManyField(blank=True, to='orders.CustomerPizza'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subOrdered',
            field=models.ManyToManyField(blank=True, to='orders.CustomerSub'),
        ),
    ]
