"""
This file consists models(structures) handling
(1). Incoming Requests Types
(2). Responses Types Sent from the server
"""

from pydantic import BaseModel


# login requests type
class LoginInModel(BaseModel):
    username: str
    password: str


# signin requests type
class SignUpModel(BaseModel):
    username: str
    email: str
    password: str
    dob: str


# response token provided
class Token(BaseModel):
    access_token: str 
    token_type: str


# update user detail request model
class UsersUpdateRequest(BaseModel):
    user_username: str
    user_email: str
    user_password: str
    user_dob: str


# this model handels create, update for post
class CreatePosts(BaseModel):
    post_title: str
    post_description: str
    post_image_url: str

