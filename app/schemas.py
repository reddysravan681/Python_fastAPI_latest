from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title:str
    content:str="content"
    published : bool=True


