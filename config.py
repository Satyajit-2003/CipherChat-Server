import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'db', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PUBLIC_KEYS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'keys')