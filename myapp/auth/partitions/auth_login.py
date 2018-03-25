#!/usr/bin/env python
# coding:utf-8
'''
file: promgen_rule.py
date: 2017/12/11 14:24
author: lockey
email: iooiooi23@163.com
github: https://github.com/LockeyCheng
csdn: http://blog.csdn.net/Lockey23
desc: 
'''

from flask import request, current_app
from flask_restful import Resource, reqparse
from myapp.auth.views import auth
from flask import render_template

__all__ = (
    'Test'
)


class Test(Resource):
    """
    """


    def get(self):
        name = ['lockey1','lockey2','lockeyx']
        return render_template('login.html', name=name)

    def post(self):

        return range(9)

auth.add_resource(Test, '/login', endpoint='s_admin_login_main')
