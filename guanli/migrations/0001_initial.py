# Generated by Django 2.1.5 on 2019-02-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='name')),
                ('img', models.CharField(max_length=128, verbose_name='img')),
                ('type', models.CharField(max_length=64, verbose_name='type')),
                ('subjection', models.CharField(max_length=64, verbose_name='subjection')),
                ('nature', models.CharField(max_length=1024, verbose_name='nature')),
                ('url', models.CharField(max_length=64, verbose_name='url')),
                ('local', models.CharField(max_length=64, verbose_name='local')),
            ],
        ),
        migrations.CreateModel(
            name='Li',
            fields=[
                ('id', models.CharField(max_length=128, verbose_name='id')),
                ('year', models.CharField(max_length=128, verbose_name='year')),
                ('low', models.CharField(max_length=128, verbose_name='low')),
                ('high', models.CharField(max_length=128, verbose_name='high')),
                ('ave', models.CharField(max_length=128, verbose_name='ave')),
                ('num', models.CharField(max_length=128, verbose_name='num')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
                ('number', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='number')),
            ],
        ),
        migrations.CreateModel(
            name='Wen',
            fields=[
                ('id', models.CharField(max_length=128, verbose_name='id')),
                ('year', models.CharField(max_length=128, verbose_name='year')),
                ('low', models.CharField(max_length=128, verbose_name='low')),
                ('high', models.CharField(max_length=128, verbose_name='high')),
                ('ave', models.CharField(max_length=128, verbose_name='ave')),
                ('num', models.CharField(max_length=128, verbose_name='num')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
                ('number', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='number')),
            ],
        ),
    ]
