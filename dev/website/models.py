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
    question = db.Column(db.String(500))
    option1 = db.Column(db.String(200))
    option2 = db.Column(db.String(200))
    option3 = db.Column(db.String(200))
    option4 = db.Column(db.String(200))
    answer = db.Column(db.String(200))

    def __repr__(self):
        return f"<Quiz_M {self.id}: {self.question}? {self.answer}"

    def get_answer_string(self):
        if self.answer == self.option1:
            return self.option1
        elif self.answer == self.option2:
            return self.option2
        elif self.answer == self.option3:
            return self.option3
        elif self.answer == self.option4:
            return self.option4
        else:
            return "Invalid answer"

    def get_option_string(self, option):
        if option == 1:
            return self.option1
        elif option == 2:
            return self.option2
        elif option == 3:
            return self.option3
        elif option == 4:
            return self.option4
        else:
            return "Invalid option"



# True or false questions
class Quiz_TF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(20))
    question = db.Column(db.String(500))
    answer = db.Column(db.String(50))
    
    def __repr__(self):
        return f"<Quiz_TF {self.id}: {self.question}? {self.answer}"

    def get_answer_string(self):
        if self.answer:
            return "True"
        else:
            return "False"

    def get_option_string(self, option):
        if option == 1:
            return "True"
        elif option == 2:
            return "False"
        else:
            return "Invalid option"