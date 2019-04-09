from django.db import models


class Hello(models.Model):
    name = models.CharField(max_length=64, primary_key=True, verbose_name='name')
    img = models.CharField(max_length=128, verbose_name='img')
    type = models.CharField(max_length=64, verbose_name='type')
    subjection = models.CharField(max_length=64, verbose_name='subjection')

    nature = models.CharField(max_length=1024, verbose_name='nature')
    url = models.CharField(max_length=64, verbose_name='url')
    local = models.CharField(max_length=64, verbose_name='local')

class Li(models.Model):
    id = models.CharField(max_length=128, verbose_name='id')
    year = models.CharField(max_length=128, verbose_name='year')
    low = models.CharField(max_length=128, verbose_name='low')
    high = models.CharField(max_length=128, verbose_name='high')
    ave = models.CharField(max_length=128, verbose_name='ave')
    num = models.CharField(max_length=128, verbose_name='num')
    type = models.CharField(max_length=128, verbose_name='type')
    number = models.CharField(max_length=128,primary_key=True,verbose_name='number')

class Wen(models.Model):
    id = models.CharField(max_length=128, verbose_name='id')
    year = models.CharField(max_length=128, verbose_name='year')
    low = models.CharField(max_length=128, verbose_name='low')
    high = models.CharField(max_length=128, verbose_name='high')
    ave = models.CharField(max_length=128, verbose_name='ave')
    num = models.CharField(max_length=128, verbose_name='num')
    type = models.CharField(max_length=128, verbose_name='type')
    number = models.CharField(max_length=128,primary_key=True,verbose_name='number')

class type1(models.Model):
    id = models.CharField(max_length=128, verbose_name='id')
    type = models.CharField(max_length=128, verbose_name='type')
    score = models.CharField(max_length=128, verbose_name='score')
    num = models.CharField(max_length=128,primary_key=True, verbose_name='num')

class type2(models.Model):
    id = models.CharField(max_length=128, verbose_name='id')
    type = models.CharField(max_length=128, verbose_name='type')
    score = models.CharField(max_length=128, verbose_name='score')
    num = models.CharField(max_length=128,primary_key=True, verbose_name='num')

class type3(models.Model):
    id = models.CharField(max_length=128, verbose_name='id')
    type = models.CharField(max_length=128, verbose_name='type')
    score = models.CharField(max_length=128, verbose_name='score')
    num = models.CharField(max_length=128,primary_key=True, verbose_name='num')




