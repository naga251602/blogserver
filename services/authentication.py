"""
This files consists of code that is used to authenticate the user
"""

from fastapi.security import (
    OAuth2PasswordRequestForm,
    OAuth2PasswordBearer,
)
from fastapi import APIRouter, Depends, HTTPException, status
from models.reqResModels import LoginInModel, Token, SignUpModel
from db.dbconnector import session
from db.queryDB import check_login_details, get_user, create_user
from .jwttoken import create_token
from config.envConfig import TOKEN_EXP_MINUTES, ALGORITHM, JWT_SECRET
from jose import JWTError, jwt


# initliazing the auth router
auth_router = APIRouter()

# defining the scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# gets current user from database if token is valid
async def get_current_user(token: Token = Depends(oauth2_scheme)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized",
        headers={"www-Authenticate": "Bearer"},
    )
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username = decoded.get("sub")

        if not username:
            raise exception
        user = get_user(username, session)
        if not user:
            raise exception
        return user
    except JWTError:
        raise exception


# login route
@auth_router.post("/token/", response_model=Token)
async def login(data: LoginInModel = Depends(OAuth2PasswordRequestForm)):
    user = {"username": data.username, "password": data.password}
    res = check_login_details(user, session)
    if isinstance(res, dict):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=res["message"]
        )
    else:
        if res == 1:
            token = create_token({"sub": data.username}, TOKEN_EXP_MINUTES)
            return {"access_token": token, "token_type": "bearer"}
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials!!"
            )


# register route
@auth_router.post("/users/register")
async def register(data: SignUpModel = Depends(OAuth2PasswordRequestForm)):
    res = create_user(data.dict(), session)
    if res["status"] == "failed":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=res["message"]
        )
    else:
        return {"message": "user created now login"}
