import time
from flask import request
from app import app, db, socketio
from app.utils import auth, buffer

active_users = {}  # username : session_id

@socketio.on('connect')
def handle_connect(data):
    if 'token' not in data:
        socketio.emit('error', {'error': 'Token not Found'}, room=request.sid)
        return
    token = data['token']
    user = auth.check_token(token)
    if user is None:
        socketio.emit('error', {'error': 'Unauthorised Access'}, room=request.sid)
        return
    active_users[user.username] = request.sid
    socketio.emit('data', {'message': 'Connected'}, room=request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    for user in active_users:
        if active_users[user] == request.sid:
            del active_users[user]
            break     
    socketio.emit('data', {'message': 'Disconnected'}, room=request.sid)

@socketio.on('message')
def handle_message(data):
    print(data)
    if 'token' not in data:
        socketio.emit('error', {'error': 'Token not Found'}, room=request.sid)
        return
    token = data['token']
    user = auth.check_token(token)
    if user is None:
        socketio.emit('error', {'error': 'Unauthorised Access'}, room=request.sid)
        return
    send_to = data['to']
    message = data['message']
    if send_to in active_users and auth.active_users[send_to] == True:
        print("Emited", message, user.username, send_to, int(time.time()))
        socketio.emit('message', {'message': message, 'from' : user.username, 'timestamp':int(time.time())}, room=active_users[send_to])
    else:
        buffer.create_message(user.username, send_to, message, int(time.time()))
