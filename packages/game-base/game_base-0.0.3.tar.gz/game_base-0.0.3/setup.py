#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='game_base',
    version='0.0.3',
    author='gamebase',
    author_email='gamebase_team@gmail.com',
    description='python game utils',
    packages=find_packages(),
    install_requires=['pymysql', 'redis', 'pycore-utils', 'flask-socketio', 'gevent-websocket', 'cryptography',
                      'pycryptodome', 'sqlalchemy', 'protobuf']
)
