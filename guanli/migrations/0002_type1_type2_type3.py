# Generated by Django 2.1.5 on 2019-02-27 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guanli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='type1',
            fields=[
                ('id', models.CharField(max_length=128, verbose_name='id')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
                ('score', models.CharField(max_length=128, verbose_name='score')),
                ('num', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='num')),
            ],
        ),
        migrations.CreateModel(
            name='type2',
            fields=[
                ('id', models.CharField(max_length=128, verbose_name='id')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
                ('score', models.CharField(max_length=128, verbose_name='score')),
                ('num', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='num')),
            ],
        ),
        migrations.CreateModel(
            name='type3',
            fields=[
                ('id', models.CharField(max_length=128, verbose_name='id')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
                ('score', models.CharField(max_length=128, verbose_name='score')),
                ('num', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='num')),
            ],
        ),
    ]
