# Generated by Django 2.2.10 on 2020-03-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_cart_cartpaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastaName', models.CharField(max_length=64)),
                ('pastaPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
