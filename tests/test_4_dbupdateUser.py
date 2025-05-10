"""
This files contains code to test user updaing the details
"""

from unittest import TestCase
from db.queryDB import create_user, update_user, get_user
from db.dbconnector import session


# a sample user data
user_1 = {
    "username": "test_user_1",
    "email": "testuser1@email.com",
    "password": "123456@@",
    "dob": "2002/12/31",
}

user_2 = {
    "username": "test_user_2",
    "email": "testuser2@email.com",
    "password": "123456@@",
    "dob": "2002/12/01",
}

# adding the users into the database
create_user(user_1, session)
create_user(user_2, session)

# getting the new test users from the db
user_1_from_db = get_user(user_1["username"], session)
user_2_from_db = get_user(user_2["username"], session)


class TestDB(TestCase):
    # testing with a new username
    def test_update_user_in_db_with_new_username(self):
        self.assertEqual(
            update_user(
                {
                    "id": user_1_from_db.user_id,
                    "user_username": "test_user_1_updated",
                    "user_email": "",
                    "user_password": "",
                    "user_dob": "",
                },
                session,
            ),
            {"message": "Updated!!", "status": "success"},
        )

    # testing with a new email that already exists
    def test_update_user_in_db_with_same_email(self):
        self.assertEqual(
            update_user(
                {
                    "id": user_1_from_db.user_id,
                    "user_username": "test_user_1_updated",
                    "user_email": "testuser2@email.com",
                    "user_password": "",
                    "user_dob": "",
                },
                session,
            ),
            {"message": "this email linked to another account", "status": "failed"},
        )

    # testing with other users's username
    def test_update_user_in_db_with_username_of_another_user(self):
        self.assertEqual(
            update_user(
                {
                    "id": user_1_from_db.user_id,
                    "user_username": "test_user_2",
                    "user_email": "testuser1@email.com",
                    "user_password": "123456@@",
                    "user_dob": "2002/12/31",
                },
                session,
            ),
            {"message": "user with this username already exists", "status": "failed"},
        )
