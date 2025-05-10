"""
This files contains code to test new user creation
"""

from unittest import TestCase
from db.queryDB import create_user
from db.dbconnector import session


# a sample user data
new_user = {
    'username': 'ram',
    'email':'ram@email.com',
    'password': 'ram123456@@',
    'dob':  "2002/12/31"
}

class TestDB(TestCase):
    def test_userCreation(self):
        # adding new user
        self.assertDictEqual(
            create_user(new_user, session),
            {"message": "user created!!", "status": "success"}
        )
