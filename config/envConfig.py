"""
this files imports all the variables from .env files
"""
from dotenv import load_dotenv
import os 


load_dotenv()

# DB
DB_URI= os.getenv('DB_URI')

# JWT
TOKEN_EXP_MINUTES= os.getenv('TOKEN_EXP_MINUTES')
ALGORITHM= os.getenv('ALGORITHM')
JWT_SECRET= os.getenv('JWT_SECRET')