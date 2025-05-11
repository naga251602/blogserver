"""
This files consists of all user endpoints execept login and register (happens in service/authentication.py)
"""

from fastapi import APIRouter, Depends
from services.authentication import get_current_user
from db.queryDB import update_user, delete_user
from db.models import Users
from db.dbconnector import connect_to_db
from typing import Annotated, Union
from models.reqResModels import UsersUpdateRequest


# intializing user router
user_router = APIRouter()
session = connect_to_db()

# route to get user details
@user_router.get("/users/details")
async def get_user_details(current_user: Users = Depends(get_current_user)):
    """
    This route is used to get current authenticated user details
    """
    return {"data": current_user}


@user_router.put("/users/update/{user_id}")
async def update_user_details(user_id:str, user: UsersUpdateRequest):
    """
    This route is used to update the user details.
    fill in the field only which you want update rest leave it as ""
    """
    data = user.dict()
    data.update({
        'id': user_id
    })
    res = update_user(data, session)
    return res


@user_router.delete('/users/update/{user_id}')
async def delete_user(user: Users = Depends(get_current_user)):
    """
    This route is used to delete the user and all posts the user has created in DB
    """
    res = delete_user(user.user_id, session)
    return res
