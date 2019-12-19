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

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user_id(email: str) -> int:
        return User.query.filter_by(email=email).first().id


class BloodPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    systolic = db.Column(db.Integer)
    diastolic = db.Column(db.Integer)
    bp_recorded_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self) -> repr:
        return f"<BloodPressure {self.systolic}/{self.diastolic}>"


class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weight = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self) -> repr:
        return f"<Weight {self.weight}>"


class NutritionInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    report_id = db.Column(db.Integer, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    meal_type = db.Column(db.)
    calories = db.Column(db.Integer)
    calories_from_fat = db.Column(db.Integer)
    total_fat = db.Column(db.Integer)
    trans_fat = db.Column(db.Integer)
    saturated_fat = db.Column(db.Integer)
    cholesterol = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    total_carbohydrate = db.Column(db.Integer)
    dietary_fiber = db.Column(db.Integer)
    sugars = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    vitamin_a = db.Column(db.Integer)
    vitamin_c = db.Column(db.Integer)
    calcium = db.Column(db.Integer)
    iron = db.Column(db.Integer)
    thiamine = db.Column(db.Integer)
    riboflavin = db.Column(db.Integer)
    niacin = db.Column(db.Integer)
    pantothenic_acid = db.Column(db.Integer)
    vitamin_b6 = db.Column(db.Integer)
    folate = db.Column(db.Integer)
    biotin = db.Column(db.Integer)
    vitamin_b12 = db.Column(db.Integer)
    vitamin_d = db.Column(db.Integer)
    vitamin_e = db.Column(db.Integer)
    vitamin_k = db.Column(db.Integer)
    phosphorus = db.Column(db.Integer)
    iodine = db.Column(db.Integer)
    magnesium = db.Column(db.Integer)
    zinc = db.Column(db.Integer)
    selenium = db.Column(db.Integer)
    copper = db.Column(db.Integer)
    manganese = db.Column(db.Integer)
    chromium = db.Column(db.Integer)
    molybdenum = db.Column(db.Integer)
    chloride = db.Column(db.Integer)

    def __repr__(self) -> repr:
        return f"<Calories {self.calories}>"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))