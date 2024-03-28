from app import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    public_key = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return '<User username=%r, email=%r>' % (self.username, self.email)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender = db.Column(db.String(80), nullable=False)
    receiver = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<BufferedMessage sender=%r, receiver=%r, message=%r>' % (self.sender, self.receiver, self.message)
    
    def json(self):
        return {'sender': self.sender, 'receiver': self.receiver, 'message': self.message, 'timestamp': self.timestamp}
    

with app.app_context():
    db.create_all()
