#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, g, jsonify, has_request_context, abort, \
    send_from_directory, send_file, url_for, current_app

try:
    from flask import _app_ctx_stack as ctx_stack
except ImportError:  # pragma: no cover
    from flask import _request_ctx_stack as ctx_stack

# Default App name
DEFAULT_APP_NAME = 'myapp'


__all__ = (
    'create_app'
)


def create_app(config_name=None):
    """ app工厂函数
    :param config_name:
    :return:
    """

    app = Flask(DEFAULT_APP_NAME)
    configure_blueprints(app)
    return app

def configure_blueprints(app):
    from .auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/admin')
    
    @app.route('/ping', methods=['GET'])
    def test_ping():
        return '<h1>www.lockey.io</h1>'
