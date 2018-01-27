# Generated by Django 2.0.1 on 2018-01-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('value', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('bar_code', models.CharField(max_length=13, unique=True, verbose_name='Código de Barras')),
            ],
        ),
    ]