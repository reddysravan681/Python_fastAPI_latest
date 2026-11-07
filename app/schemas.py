from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
from pydantic.types import conint
#Creating different models for different type of requests
class PostBase(BaseModel):
    title:str
    content:str
    published : bool=True

class Createpost(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
            from_attributes=True
#-->models for response



class UserCreate(BaseModel):
    email:EmailStr
    password:str      
    phone_number:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
            from_attributes=True

class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut

    class Config:
        from_attributes=True
                    
class PostOut(BaseModel):
     post:Post
     votes:int    

     class Config:
        from_attributes=True            


class UserLogin(BaseModel):
     email:EmailStr
     password:str            


class Token(BaseModel):
    access_token:str 
    token_type:str

class TokenData(BaseModel):
    id:Optional[int]=None         




class Vote(BaseModel):
     post_id:int
     dir:conint(le=1)

