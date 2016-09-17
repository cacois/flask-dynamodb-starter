import os
import unittest
import coverage

from flask_script import Manager

COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'app/tests/*',
        'app/server/config.py',
        'app/server/*/__init__.py'
    ]
)
COV.start()

from app.server import app, db
from app.server.models import User

manager = Manager(app)

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1

@manager.command
def create_db():
    """Creates the db tables."""
    db.create_schema()

@manager.command
def drop_db():
    """Drops the db tables."""
    db.delete_schema()

@manager.command
def create_admin():
    """Creates the admin user."""
    db.save(User(email='ad@min.com', password='admin', admin=True))

@manager.command
def create_data():
    """Creates sample data."""
    pass

if __name__ == '__main__':
    manager.run()
