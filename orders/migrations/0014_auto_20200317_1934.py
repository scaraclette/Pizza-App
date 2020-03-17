# Generated by Django 2.2.10 on 2020-03-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200317_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platterSize', models.CharField(choices=[('s', 'small'), ('l', 'large')], max_length=1)),
                ('platterName', models.CharField(max_length=64)),
                ('platterPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='platterOrdered',
            field=models.ManyToManyField(blank=True, to='orders.CustomerPlatter'),
        ),
    ]