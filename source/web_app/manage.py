#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from mainapp.app import create_app
from mainapp.database import db
from mainapp.settings import ProdConfig
from mainapp.user.models import User
from flask_script import Manager, Shell, Server
from flask_script.commands import Clean, ShowUrls

app = create_app(ProdConfig)
print('hi')
# if first user set it as administrator and create if not exists
if os.path.isfile('/poestat/secure/db.sqlite'):
    print('hi2')
    pass
else:
    print('hi3')
    db.create_all()
    print('hi4')
HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == '__main__':
    manager.run()
