"""
This files contains code to test user updaing the details
"""

from unittest import TestCase
from db.queryDB import get_user, delete_user
from db.dbconnector import session


user_1 = {
    "username": "test_user_1",
    "email": "testuser1@email.com",
    "password": "123456@@",
    "dob": "2002/12/31",
}

# after running test case 4 the user_1 is already on DB
# so need to create user again
# getting the new test users from the db
user_1_from_db = get_user(user_1["username"], session)


class TestDB(TestCase):
    # deleting user with a invlaid username
    def test_delete_user_in_db_with_invalidusername(self):
        self.assertEqual(
            delete_user("1234jfsjkfjf", session),
            {"message": "Invalid User", "status": "failed"},
        )

    def test_delete_user_with_valid_username(self):
        self.assertEqual(
            delete_user(user_1_from_db.user_id, session),
            {"message": "User deleted!!!", "status": "success"},
        )
