from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
    
from app import routes
from app import socket
