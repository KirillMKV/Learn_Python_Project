import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'kjnejgvnejnrvekjrnvwnv'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'db_project')
SQLALCHEMY_TRACK_MODIFICATIONS = False