#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student.settings')

import django

django.setup()

import json
import argparse
import random
import datetime
import codecs
import os.path as op
from guanli.models import Hello,Li,Wen,type1,type2,type3
from django.contrib.auth.models import User

from faker import Factory

fake = Factory.create('zh_CN')






'''
def init_book_data():
    with codecs.open('gaoxiao.json', 'r', 'utf-8') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'web' in b and b['web']:
            print(b)
            try:
                B = Book.objects.get_or_create(web=b['web'],image=b['image'], position=b['position'], style=b['style'])[0]
                B.Belong = b['Belong']
                B.education = b['education']
                B.schoolweb = b['schoolweb']
                #B.quantity = random.randint(0, 7)
                B.save()
            except KeyError:
                continue
'''

def hello():
    with codecs.open('school_data.json', 'r', 'utf-8-sig') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'id' in b and b['id']:
            print(b)
            try:
                B = Hello.objects.get_or_create(name=b['id'],img=b['school_img'], type=b['school_type'], subjection=b['school_subjection'])[0]
                B.nature = b['school_nature']
                B.url = b['school_url']
                B.local = b['local_name']
                #B.quantity = random.randint(0, 7)
                B.save()
            except KeyError:
                continue

def li():
    with codecs.open('school_li.json', 'r', 'utf-8-sig') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'number' in b and b['number']:
            print(b)
            try:
                B = Li.objects.get_or_create(id=b['id'], year=b['year'], low=b['low'],
                                                high=b['high'],ave = b['ave'],number=b['number'],
                                             num=b['num'],type = b['type'])[0]
                #B.ave = b['ave']
                #B.number=b['number']
                #B.num = b['num']
                #B.type = b['type']
                #B.quantity = random.randint(0, 7)
                B.save()
            except KeyError:
                continue

def wen():
    with codecs.open('school_wen.json', 'r', 'utf-8-sig') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'number' in b and b['number']:
            print(b)
            try:
                B = Wen.objects.get_or_create(id=b['id'], year=b['year'], low=b['low'],
                                                high=b['high'],ave = b['ave'],number=b['number'],
                                             num=b['num'],type = b['type'])[0]
                #B.ave = b['ave']
                #B.number=b['number']
                #B.num = b['num']
                #B.type = b['type']
                #B.quantity = random.randint(0, 7)
                B.save()
            except KeyError:
                continue

def one():
    with codecs.open('type1.json', 'r', 'utf-8-sig') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'num' in b and b['num']:
            print(b)
            try:
                B = type1.objects.get_or_create(id=b['id'], type=b['type'], score=b['score'],
                                                num=b['num'])[0]
                B.save()
            except KeyError:
                continue

def two():
    with codecs.open('type2.json', 'r', 'utf-8-sig') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'num' in b and b['num']:
            print(b)
            try:
                B = type2.objects.get_or_create(id=b['id'], type=b['type'], score=b['score'],
                                                num=b['num'])[0]
                B.save()
            except KeyError:
                continue

def three():
    with codecs.open('type3.json', 'r', 'utf-8-sig') as f:
        gaoxiao = json.load(f)

    for b in gaoxiao:
        if 'num' in b and b['num']:
            print(b)
            try:
                B = type3.objects.get_or_create(id=b['id'], type=b['type'], score=b['score'],
                                                num=b['num'])[0]
                B.save()
            except KeyError:
                continue


if __name__ == '__main__':
    #init_book_data()
    #hello()
    #li()
    #wen()
    #one()
    two()
    three()

    ''' 
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help=u"你要生成的数据")
    args = parser.parse_args()

    if args.data == 'all':
        init_book_data()
    elif args.data == 'book':
        init_book_data()
    '''
