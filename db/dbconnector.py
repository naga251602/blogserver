"""
This files provides the session to query the databse
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
from config.envConfig import DB_URI


# function to give connection to db
def connect_to_db() -> Session:
    try:
        # creating connection
        engine = create_engine(DB_URI)
        print(DB_URI)

        # create all tables in the database if not exists
        Base.metadata.create_all(engine)

        # creating common session for all server-DB actions
        Session = sessionmaker(bind=engine)
        session = Session()

        return session

    except Exception as err:
        print(f"[*] Exception in DB: {err}")
