import unittest
import os
import json
from app import create_app, db
from app.models import User, Weight, BloodPressure
from random import randint

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

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_add_weight(self) -> None:
        """ Test A new weight can be added """
        u = User(username="test", email="test@test.com")
        db.session.add(u)
        db.session.commit()
        w = Weight(weight=randint(100, 999), weight_patient=u)
        db.session.add(w)
        db.session.commit()
        self.assertEqual(User.query.first_or_404().username, 'test')
        #res = self.client().post('/weight/add')


if __name__ == "__main__":
    unittest.main()