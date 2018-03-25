#!/usr/bin/env python
#coding:utf-8
'''
file: __init__.py.py
date: 2017/12/7 16:41
author: lockey
email: iooiooi23@163.com
github: https://github.com/LockeyCheng
csdn: http://blog.csdn.net/Lockey23
desc: 
'''
import os, yaml
os.environ.setdefault('Promgen_conf_dir', os.path.expanduser('~/.config/promgen'))
CONFIG_DIR = os.environ['Promgen_conf_dir']
PROMGEN_CONFIG = os.path.join(CONFIG_DIR, 'promgen.yml')
PROMETHEUS_CONFIG = os.path.join(CONFIG_DIR, 'prometheus.yml')
ALERTMANAGER_CONFIG = os.path.join(CONFIG_DIR, 'alertmanager.yml')

if os.path.exists(PROMGEN_CONFIG):
    with open(PROMGEN_CONFIG) as fp:
        PROMGEN = yaml.load(fp)
else:
    PROMGEN = {}

