import unittest
import os
import json
from app import create_app, db
from app.models import User, Weight, BloodPressure
from random import randint
from werkzeug.exceptions import NotFound

class HealthCheckerTestCase(unittest.TestCase):
    """ HealthChecker Test Case """

    def setUp(self) -> None:
        """ Define Test Variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self) -> None:
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_user_add(self) -> None:
        u = User(username="test", email="test@test.com")
        db.session.add(u)
        db.session.commit()
        test_user = User.query.first_or_404()
        self.assertEqual(test_user.username, 'test')
        self.assertEqual(test_user.email, 'test@test.com')
        self.assertEqual(test_user.id, 1)

    def test_add_weight(self) -> None:
        """ Test A new weight can be added """
        u = User(username="test", email="test@test.com")
        db.session.add(u)
        db.session.commit()
        random_weight = randint(100, 999)
        w = Weight(weight=random_weight, weight_patient=u)
        db.session.add(w)
        db.session.commit()
        test_user = User.query.first_or_404()
        for weight in test_user.weights:
            self.assertEqual(str(weight), f"<Weight {random_weight}>")

    def test_add_blood_pressure(self) -> None:
        u = User(username="test", email="test@test.com")
        db.session.add(u)
        db.session.commit()
        rand_systolic = randint(0, 300)
        rand_diastolic = randint(0, 300)
        bp = BloodPressure(systolic=rand_systolic, diastolic=rand_diastolic, pressure_patient=u)
        db.session.add(bp)
        db.session.commit()
        test_user = User.query.first_or_404()
        for bp in test_user.pressures:
            self.assertEqual(bp.systolic, rand_systolic)
            self.assertEqual(bp.diastolic, rand_diastolic)

    def test_user_removal(self) -> None:
        # Add the user
        u = User(username="testdelete", email="pleasedeleteme@deleteme.com")
        db.session.add(u)
        db.session.commit()
        # Verify user exists
        test_user = User.query.first_or_404()
        self.assertEqual(test_user.username, 'testdelete')
        self.assertEqual(test_user.email, 'pleasedeleteme@deleteme.com')
        user = User.query.filter_by(username='testdelete').one()
        db.session.delete(user)
        db.session.commit()
        with self.assertRaises(NotFound):
            print(User.query.first_or_404())


if __name__ == "__main__":
    unittest.main()