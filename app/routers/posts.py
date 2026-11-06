from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PostBase,Createpost,Post,PostOut
from fastapi import Depends,HTTPException,status,Response,APIRouter
from app.models import Post as PostModel,Vote
from app.oauth2 import get_current_user
from typing import Optional
from sqlalchemy import func
router=APIRouter(
    prefix="/posts",
    tags=["posts"]
)

##Endpoint to get all the posts 
#@router.get('/',response_model=list[Post])
#,response_model=list[PostOut]
@router.get('/',response_model=list[PostOut])
def get_posts(db:Session=Depends(get_db),current_user:int=Depends(get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    #posts=db.query(PostModel).filter(PostModel.title.contains(search)).limit(limit).offset(skip).all()
    posts=db.query(PostModel,
                    func.count(Vote.post_id).label("Votes")).join(
                        Vote,Vote.post_id==PostModel.id,isouter=True).group_by(PostModel.id).filter(
                            PostModel.title.contains(search)).limit(limit).offset(skip).all()
        
    return [
        {"post": post, "votes": votes}
        for post, votes in posts
    ]
    
##Endpoint to get a post using post ID 
@router.get("/{id}",response_model=PostOut)
def get_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    #post=db.query(PostModel).filter(PostModel.id==id).first()
    result=db.query(PostModel,
                        func.count(Vote.post_id).label("Votes")).join(
                            Vote,Vote.post_id==PostModel.id,isouter=True).group_by(PostModel.id).filter(PostModel.id==id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found in the database")

    post, votes = result

    return {"post": post, "votes": votes}
##to get the current user's posts
@router.get("/{id}",response_model=Post)
def get_posts(id:int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    post=db.query(PostModel).filter(PostModel.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found in the database")

    return post 
    
    
##Endpoint to create a post -->3
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=Post)
def create_post(post:Createpost,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    ##new_post=models.Post(title=post.title,content=post.content,published=post.published)
    owner_id=current_user
    new_post=PostModel(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
 

##Endpoint to Delete a post with certain ID
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleting_post(id : int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    post_query=db.query(PostModel).filter(PostModel.id==id)
    post=post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

#Endpoint to updata a post with certain ID
@router.put("/{id}",response_model=Post)
def update_post(id:int,post:Createpost,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):

    post_query=db.query(PostModel).filter(PostModel.id==id)
    db_post=post_query.first()
    if db_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"there is no post with id = {id}")
    if id!=current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    post_query.update(post.dict())
    db.commit()
    return post_query.first()