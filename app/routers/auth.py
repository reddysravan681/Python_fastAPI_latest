from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserLogin
from app.models import Users
from app import utils
from app.oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.schemas import Token


router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db),response_model=Token):
    user=db.query(Users).filter(Users.email==user_credentials.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")

    ##creating a jwt token and return it
    access_token=create_access_token(data={'user_id':user.id})


    return {'access_token':access_token,"token_type":'Bearer'}

    
