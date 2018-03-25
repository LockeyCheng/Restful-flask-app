#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from flask_migrate import Migrate, MigrateCommand
from myapp import create_app
import myapp
import os

__all__ = (
    'app',
)


config_name = os.environ.get('APP_CFG') or 'default'

app = create_app(config_name)

if __name__ == '__main__':
    app.run()
