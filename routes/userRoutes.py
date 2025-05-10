"""
This files consists of all user endpoints execept login and register (happens in service/authentication.py)
"""

from fastapi import APIRouter, Depends
from services.authentication import get_current_user
from db.queryDB import update_user, delete_user
from db.models import Users
from db.dbconnector import session
from typing import Annotated, Union
from models.reqResModels import UsersUpdateRequest


# intializing user router
user_router = APIRouter()


# route to get user details
@user_router.get("/users/details")
async def getItems(current_user: Users = Depends(get_current_user)):
    return {"data": current_user}


@user_router.put("/users/update/{user_id}")
async def upDateUserDetails(user_id:str, user: UsersUpdateRequest):
    data = user.dict()
    data.update({
        'id': user_id
    })
    res = update_user(data, session)
    return res


@user_router.delete('/users/update/{user_id}')
async def deleteUserDetails(user: Users = Depends(get_current_user)):
    res = delete_user(user.user_id, session)
    return res
