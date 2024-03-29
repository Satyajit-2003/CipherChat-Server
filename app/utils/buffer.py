from app import db
from app.models import Message

def create_message(sender, receiver, message, timestamp):
    msg = Message(sender=sender, receiver=receiver, message=message, timestamp=timestamp)
    db.session.add(msg)
    db.session.commit()

def get_messages(username): 
    messages = Message.query.filter_by(receiver=username).all()
    for message in messages:
        db.session.delete(message)
    return messages