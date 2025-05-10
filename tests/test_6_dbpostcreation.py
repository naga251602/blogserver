"""
This files tests whether a post is created successfully
"""

from unittest import TestCase
from db.queryDB import create_posts
from db.models import Posts
from db.dbconnector import session
from db.queryDB import get_user


user_2 = {
    "username": "test_user_2",
    "email": "testuser2@email.com",
    "password": "123456@@",
    "dob": "2002/12/01",
}

user_2_from_db = get_user(user_2["username"], session)


class PostsCreationTest(TestCase):

    def test_create_post(self):
        new_post = {}
        new_post["post_title"] = "this is a test post"
        new_post["post_description"] = "this is test post description"
        new_post["user_id"] = user_2_from_db.user_id
        new_post["post_image_url"] = ""

        self.assertDictEqual(
            create_posts(new_post, session),
            {"message": "post created!!", "status": "success"},
        )
