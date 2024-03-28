from flask import request, jsonify
from app import app
from app.utils import auth, buffer
from flask import send_file

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username').lower()
    password = request.form.get('password')
    print(username, password)    
    token = auth.login(username, password)
    if token is not None:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Unauthorised Access'}), 401
    
@app.route('/logout', methods=['POST'])
def logout():
    token = request.form.get('token')
    auth.logout(token)
    return jsonify({'message': 'Logged out'}), 200

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username').lower()
    password = request.form.get('password')
    email = request.form.get('email')
    public_key = request.form.get('public_key')
    
    if auth.register(username, password, email, public_key):
        return jsonify({'message': 'Registered'}), 200
    else:
        return jsonify({'error': 'Registration Failed'}), 401

@app.route('/get_user', methods=['POST'])
def get_user():
    token = request.form.get('token')
    user = auth.check_token(token)
    if user is not None:
        return jsonify(str(user)), 200
    else:
        return jsonify('Unauthorised Access'), 401

@app.route('/get_public_key', methods=['GET'])
def get_public_key():
    username = request.args.get('user')
    public_key = auth.get_public_key(username)
    if public_key is None:
        return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'public_key': public_key}), 200
    
@app.route('/get_messages', methods=['POST'])
def get_messages():
    token = request.form.get('token')
    user = auth.check_token(token)
    if user is None:
        return jsonify({'error': 'Unauthorised Access'}), 401
    messages = buffer.get_messages(user.username)
    return jsonify([msg.json() for msg in messages]), 200

@app.route('/users', methods=['POST'])
def users():
    token = request.form.get('token')
    user = auth.check_token(token)
    if user is None:
        return jsonify({'error': 'Unauthorised Access'}), 401
    active_users = []
    for user_, status in auth.active_users.items():
        if user_ == user.username:
            continue
        active_users.append({'user': user_, 'status': status})
    return jsonify(active_users), 200
    
