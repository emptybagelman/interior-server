from flask import current_app
from datetime import datetime
from application import db
from application.blueprints.users.model import Users
from application.blueprints.rooms.model import Rooms

class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    initial_comment = db.Column(db.Boolean, nullable = False, default = True)
    username = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable = False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable = False)
    parent_id = db.Column(db.Integer, nullable = True)
    root_id = db.Column(db.Integer, nullable = True)

    user = db.relationship("Users", backref = db.backref("comments",lazy=True))
    room = db.relationship("Rooms", backref = db.backref("comments",lazy=True))

    def __repr__(self):
        return f"Comments(id:{self.id}, comment:{self.comments}, date:{self.date}, initial_comment:{self.initial_comment}, parent_id:{self.parent_id},username:{self.username}, user_id:{self.user_id} room_id:{self.room_id} root_id:{self.root_id})"
    
    @property
    def json(self):
        return { "id": self.id, "comment": self.comment, "date":self.date, "initial_comment":self.initial_comment, "username":self.username,"user_id":self.user_id, "room_id":self.room_id, "parent_id":self.parent_id, "root_id":self.root_id }