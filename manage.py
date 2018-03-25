#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask_script import Manager, Shell, Server, prompt, prompt_pass
# from flask_migrate import Migrate, MigrateCommand
from myapp import create_app
import myapp
import os

__all__ = (
    'app',
)


config_name = os.environ.get('APP_CFG') or 'default'

app = create_app(config_name)

manager = Manager(app)

# manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


if __name__ == '__main__':
    manager.run(default_command='runserver')
