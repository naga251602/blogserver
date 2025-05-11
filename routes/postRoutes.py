"""
This file consists of endpoints to all posts CRUD
"""

from fastapi import APIRouter, Depends
from db.models import Users, Posts
from services.authentication import get_current_user
from db.queryDB import create_post, get_all_posts_by_user_id, update_post, delete_post
from models.reqResModels import CreatePosts
from db.dbconnector import connect_to_db


# initalizing router
post_router = APIRouter()
session = connect_to_db()


# route to get all the posts
@post_router.get("/posts/user/{user_id}")
async def get_posts(user: Users = Depends(get_current_user)):
    """
    This route is used to get ALL posts specific to a user id
    """
    res = get_all_posts_by_user_id(user.user_id, session)
    return res


# route to crate new posts
@post_router.post("/posts/create")
async def create_post(post: CreatePosts, user: Users = Depends(get_current_user)):
    """
    This is route is used to create a new post
    """
    new_post = Posts()
    new_post.post_title = post.post_title
    new_post.post_description = post.post_description
    new_post.post_image_url = post.post_image_url
    new_post.user_id = user.user_id
    return create_post(new_post.__dict__, session)


# route to update the posts
@post_router.put("/posts/update/{post_id}")
async def update_posts(
    post_id: str, post: CreatePosts, user: Users = Depends(get_current_user)
):
    """
    This route is used to update a post. fill in the field only which you want update rest leave it as ""
    """
    new_post = Posts()
    new_post.post_id = post_id
    new_post.post_title = post.post_title
    new_post.post_description = post.post_description
    new_post.post_image_url = post.post_image_url
    new_post.user_id = user.user_id
    return update_post(new_post.__dict__, session)


# route to delete the posts
@post_router.delete("/posts/delete/{post_id}")
async def delete_posts(post_id: str, user: Users = Depends(get_current_user)):
    """
    This route is used to delete a post by id
    """
    return delete_post(post_id, session)
