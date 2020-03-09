# Generated by Django 2.0.3 on 2020-03-09 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastaName', models.CharField(max_length=64)),
                ('pastaPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaType', models.CharField(choices=[('R', 'regular'), ('S', 'sicilian')], max_length=1)),
                ('pizzaSize', models.CharField(choices=[('s', 'small'), ('l', 'large')], max_length=1)),
                ('pizzaPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platterSize', models.CharField(choices=[('s', 'small'), ('l', 'large')], max_length=1)),
                ('platterName', models.CharField(max_length=64)),
                ('platterPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saladName', models.CharField(max_length=64)),
                ('saladPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subSize', models.CharField(choices=[('s', 'small'), ('l', 'large')], max_length=1)),
                ('subName', models.CharField(max_length=64)),
                ('subPrice', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='sub',
            name='subTopping',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizzaTopping',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='cart',
            name='pizzaOrdered',
            field=models.ManyToManyField(blank=True, to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='cart',
            name='subOrdered',
            field=models.ManyToManyField(blank=True, to='orders.Sub'),
        ),
    ]
