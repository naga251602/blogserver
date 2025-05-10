"""
This file contins the code that generates the JWT tokens
"""

from jose import jwt
from datetime import timedelta, datetime, timezone
from config.envConfig import JWT_SECRET, ALGORITHM


# this function returns the token
def create_token(data: dict, exp_delta: timedelta | None = None):
    to_encode = data.copy()

    # checking if default expiration time is there
    if exp_delta:
        exp = datetime.now(timezone.utc) + timedelta(minutes=int(exp_delta.split()[0]))
    else:
        exp = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({
        'exp': exp
    })

    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)