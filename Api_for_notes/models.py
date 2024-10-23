from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timezone
import pytz

europe_timezone = pytz.timezone('Europe/Warsaw')

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), default="Title")
    content = db.Column(db.String(200))
    creation_date = db.Column(db.DateTime, default=lambda: datetime.now(europe_timezone))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))