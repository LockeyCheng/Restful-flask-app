#!/usr/bin/env python
#coding:utf-8
'''
file: views.py
date: 2017/12/7 16:47
author: lockey
email: iooiooi23@163.com
github: https://github.com/LockeyCheng
csdn: http://blog.csdn.net/Lockey23
desc: 
'''
from flask import Blueprint
from flask_restful import Api

__all__ = [
    'auth',
    'auth_blueprint'
]
auth_blueprint = Blueprint('auth', __name__,template_folder='templates')

auth = Api(auth_blueprint)
import partitions
