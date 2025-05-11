"""
This file handles all the queries that happens on DB
"""

from .models import Users, Posts
from sqlalchemy.orm import Session
from sqlalchemy import or_
from uuid import uuid4
from passlib.hash import sha256_crypt
from datetime import date


# creating new user
def create_user(user: dict, session: Session) -> dict:
    """
    This function creates users in the database after checking if user with email and user name exists.
    """

    # checking if user existing in the db
    usr = (
        session.query(Users)
        .filter(
            or_(
                Users.user_username == user["username"],
                Users.user_email == user["email"],
            )
        )
        .first()
    )

    if usr:
        return {"message": "user already exists!!", "status": "failed"}
    else:
        new_user = Users()
        new_user.user_username = user["username"]
        new_user.user_email = user["email"]
        new_user.user_id = uuid4()
        new_user.user_password = sha256_crypt.hash(user["password"])
        year, month, day = list(map(int, user["dob"].split("/")))
        new_user.user_dob = date(year=year, month=month, day=day)
        session.add(new_user)
        session.commit()
        return {"message": "user created!!", "status": "success"}


# check userlogin details match
def check_login_details(user: dict, session: Session) -> dict | bool:
    """
    this function is used to check validate the login details if user exists in db it return bool, else it returns a dict with { "message":"", "status":True | False }
    """
    usr = get_user(user["username"], session)
    if not usr:
        return {"message": "User does not exists", "status": "failed"}
    return sha256_crypt.verify(user["password"], usr.user_password)


# get user by username
def get_user(username: str, session: Session) -> Users | None:
    """
    This function is used to fetch the user details from the database
    """
    user = session.query(Users).filter(Users.user_username == username).first()
    if not user:
        return None
    return user


# update the user in the database
def update_user(data: dict, session: Session) -> dict:
    # checking if user exists
    user = session.query(Users).filter(Users.user_id == data["id"]).first()
    if not user:
        return {"message": "user does not exist", "status": "failed"}

    # cheking if updated username or email already exist in the db for other users
    if data["user_username"] != "":
        user_by_username = (
            session.query(Users)
            .filter(Users.user_username == data["user_username"])
            .first()
        )

        if user_by_username:
            return {
                "message": "user with this username already exists",
                "status": "failed",
            }
        else:
            user.user_username = data["user_username"]

    if data["user_email"] != "":
        user_by_email = (
            session.query(Users).filter(Users.user_email == data["user_email"]).first()
        )

        if user_by_email:
            return {
                "message": "this email linked to another account",
                "status": "failed",
            }
        else:
            user.user_email = data["user_email"]

    if data["user_password"] != "":
        user.user_password = sha256_crypt.hash(user.user_username)

    if data["user_dob"] != "":
        user.user_dob = data["user_dob"]

    # saving the data to DB
    session.commit()
    return {"message": "Updated!!", "status": "success"}


# delete user account from DB
def delete_user(user_id: str, session: Session):
    user = session.query(Users).filter(Users.user_id == user_id).first()
    posts = session.query(Posts).filter(Posts.user_id == user_id).all()

    if not user:
        return {"message": "Invalid User", "status": "failed"}
    else:
        # deleting the user and posts they have created
        session.delete(user)
        session.delete(posts)
        session.commit()
        return {"message": "User deleted!!!", "status": "success"}


# posts actions


# this function create new posts
def create_post(post: dict, session: Session) -> dict:
    new_post = Posts()
    new_post.post_id = uuid4()
    new_post.post_title = post["post_title"]
    new_post.post_description = post["post_description"]
    new_post.user_id = post["user_id"]
    new_post.post_image_url = post["post_image_url"] or ""

    session.add(new_post)
    session.commit()

    return {"message": "post created!!", "status": "success"}


# get all the posts of a specific user
def get_all_posts_by_user_id(user_id: str, session: Session):
    result = session.query(Posts).filter(Posts.user_id == user_id).all()
    return {"posts": result}


# this function is used to update the posts
def update_post(updatedPost: dict, session: Session) -> dict:

    post = session.query(Posts).filter(Posts.post_id == updatedPost["post_id"]).first()

    # checking if the post exists
    if post is None:
        return {"message": "post not found!!", "status": "failed"}

    post.post_title = updatedPost["post_title"] or post.post_title
    post.post_description = updatedPost["post_description"] or post.post_description
    post.post_image_url = updatedPost["post_image_url"] or post.post_image_url

    session.commit()
    return {"message": "post Updated!!", "status": "success"}


# this function deletes the post
def delete_post(post_id: str, session: Session) -> dict:

    post = session.query(Posts).filter(Posts.post_id == post_id).first()

    # check if post exists before deleting
    if post is None:
        return {"message": "post not found!!", "status": "failed"}

    session.delete(post)
    session.commit()
    return {"message": "post deleted!!", "status": "success"}
