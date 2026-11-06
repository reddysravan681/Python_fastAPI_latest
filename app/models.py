from app.database import Base
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,text,ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):

    __tablename__="posts"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String(255),nullable=False)
    content=Column(String(255),nullable=False)
    published = Column(Boolean, nullable=False, server_default=text("TRUE"))
    created_at = Column(TIMESTAMP,nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE",onupdate="CASCADE"),nullable=False)
    owner=relationship("Users")


class Users(Base):
    __tablename__='users'
    email=Column(String(255),nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    id=Column(Integer,primary_key=True,nullable=False)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    phone_number=Column(String(255))


class Vote(Base):
    __tablename__='votes'
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)



