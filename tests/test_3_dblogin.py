from unittest import TestCase
from db.queryDB import checkloginDetails
from db.dbconnector import session


# a sample user data
login_details = {
    "username": "ram",
    "password": "ram123456@@",
}


class TestDB(TestCase):
    # this test checks with a right password
    def test_checkCredential_1(self):
        self.assertEqual(checkloginDetails(login_details, session), True)

    # this test checks with a wrong password
    def test_checkCredential_2(self):
        data = login_details.copy()
        data.update({"password": "1234"})
        self.assertEqual(checkloginDetails(data, session), False)

    # # this test checks with a username that does not exists in the DB
    def test_checkCredentail_3(self):
        data = login_details.copy()
        data.update({"username": "ravi"})

        self.assertDictEqual(
            checkloginDetails(data, session),
            {"message": "User does not exists", "status": "failed"},
        )