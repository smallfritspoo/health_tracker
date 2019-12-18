from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    weights = db.relationship('Weight', backref='weight_patient', lazy='dynamic')
    pressures = db.relationship('BloodPressure', backref='pressure_patient', lazy='dynamic')

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class BloodPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    systolic = db.Column(db.Integer)
    diastolic = db.Column(db.Integer)
    bp_recorded_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<BloodPressure {self.systolic}/{self.diastolic}>"


class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weight = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Weight {self.weight}>"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))