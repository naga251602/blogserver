"""
this files is used to
(1) define, create and add tables to the DB
"""

from sqlalchemy import Column, String, Boolean, DATE
from sqlalchemy.orm import declarative_base


Base = declarative_base()


# users table
class Users(Base):
    # table name
    __tablename__ = "users"

    # columns
    user_id = Column(String(400), primary_key=True)
    user_username = Column(String(20), nullable=False)
    user_email = Column(String(100), nullable=False)
    user_password = Column(String(500), nullable=False)
    user_dob = Column(DATE, nullable=False)
    isAdmin = Column(Boolean, nullable=False, default=False)
    disabled = Column(Boolean, nullable=False, default=False)


# posts table
class Posts(Base):
    # table name
    __tablename__ = "posts"

    # columns
    post_id = Column(String(400), primary_key=True)
    user_id = Column(String(400), nullable=False)
    post_title = Column(String(300), nullable=False)
    post_description = Column(String(2000), nullable=False)
    post_image_url = Column(String(1000), nullable=True, default="")
