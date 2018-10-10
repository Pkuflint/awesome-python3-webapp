#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'
    name = StringField()
    id = IntegerField(primary_key=True)

user = User(id=123, name='bing')
user.insert()
users = User.findall()