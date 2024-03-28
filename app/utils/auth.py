import datetime
from app.models import User
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

logged_out_tokens = []
active_users = {}
with app.app_context():
    for user in User.query.all():
        active_users[user.username] = False

def clear_expired_tokens():
    for token in logged_out_tokens:
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            if data["exp"] < datetime.datetime.now(datetime.timezone.utc):
                logged_out_tokens.remove(token)
        except:
            logged_out_tokens.remove(token)
    return True

def generate_token(user):
    clear_expired_tokens()
    return jwt.encode(
            {
                "user_id": user.username,
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2),
            },
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )

def check_token(token):
    try:
        if token in logged_out_tokens:
            print("Logged out")
            return None
        data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        print(data)
        return User.query.filter_by(username=data["user_id"]).first()
    except:
        print("Invalid token")
        return None

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None and check_password_hash(user.password, password):
        active_users[username] = True
        return generate_token(user)
    else:
        return None
    
def logout(token):
    user = check_token(token)
    if user is not None:
        active_users[user.username] = False
    logged_out_tokens.append(token)
    return True

def register(username, password, email, public_key):
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username, password=generate_password_hash(password), 
                    email=email, public_key=public_key)
        db.session.add(user)
        db.session.commit()
        return True
    else:
        return False

def get_public_key(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return user.public_key
    return None    
    