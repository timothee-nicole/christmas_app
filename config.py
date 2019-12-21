import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://admin:onepassword@my-present-db.c3dqwisxqhwr.eu-west-1.rds.amazonaws.com/db'
    SQLALCHEMY_TRACK_MODIFICATIONS =False

