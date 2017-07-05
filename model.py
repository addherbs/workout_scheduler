from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://addherbs:hahahehe@mydb.cicid6gi032j.us-east-2.rds.amazonaws.com/workout'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password_hash = db.Column(db.Unicode(50))
    unites = db.Column(db.String(3))
    workouts = db.relationship('Workout', backref='user', lazy='dynamic')

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)
    bodyweight = db.Column(db.Numeric)
    exercises = db.relationship('Exercises', backref='workout', lazy='dynamic')

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id  =db.Column(db.Integer, db.ForeignKey('workout.id'))
    order = db.Column(db.Integer, unique=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    sets = db.relationship('Set', backref='exercise', lazy='dynamic')

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oder = db.Column(db.Integer , unique=True)
    weight = db.Column(db.Numeric)
    reps = db.Column(db.Integer)
    exercise_id  = db.Column(db.Integer, db.ForeignKey('exercise.id'))

if __name__ == '__main__':
    manager.run()
