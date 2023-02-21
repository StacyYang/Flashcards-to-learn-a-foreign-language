from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


# one to many relationship with User
# Notes that to be shown in study mode
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Note {self.data}>'


# one to many relationship with User
# scores 
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Note {self.score}>'



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes= db.relationship('Note')
    scores= db.relationship('Score')

    def __repr__(self):
        return f'<Note {self.username}>'


# Tester user
# username: tester
# email: test@gmail.com 
# password: 1234567


# Multiple choices questions
class Quiz_M(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(20))
    question = db.Column(db.String(500, collation='utf8mb4_unicode_ci'))
    option1 = db.Column(db.String(200, collation='utf8mb4_unicode_ci'))
    option2 = db.Column(db.String(200, collation='utf8mb4_unicode_ci'))
    option3 = db.Column(db.String(200, collation='utf8mb4_unicode_ci'))
    option4 = db.Column(db.String(200, collation='utf8mb4_unicode_ci'))
    answer = db.Column(db.String(200, collation='utf8mb4_unicode_ci'))

    def __repr__(self):
        return f"<Quiz_M {self.id}: {self.question}? {self.answer}"



# True or false questions
class Quiz_TF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(20))
    question = db.Column(db.String(500, collation='utf8mb4_unicode_ci'))
    is_true = db.Column(db.Boolean)
    
    def __repr__(self):
        return f"<Quiz_TF {self.id}: {self.question}? {self.is_true}"