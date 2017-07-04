from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://username:password@hostID/tempdatabase'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password_hash = db.Column(db.Unicode(50))
    unites = db.Column(db.String(3))

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)

class Excercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Excercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id  =db.Column(db.Integer, db.ForeignKey('workout.id'))
    order = db.Column(db.Integer, unique=True)
    excercise_id = db.Column(db.Integer, db.ForeignKey('excercise.id'))

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oder = db.Column(db.Integer , unique=True)
    weight = db.Column(db.Numeric)
    reps = db.Column(db.Integer)
