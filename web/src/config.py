import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'abc')
    PORT = os.environ.get('APP_PORT', 9090)
