from fastapi import FastAPI,Depends
from fastapi.params import Body
from app.schemas import Post
from random import randrange
from fastapi import Response,status,HTTPException
from app.sql_conn import connection,cursor

#creating the object of fastAPI
app=FastAPI()


#Dummy DB used before actual database
my_posts=[
    {
        "title":"title of post 1",
        "content":"content of the post 1",
        "id":1  
    },
    {
            "title":"title of post 2",
            "content":"content of the post 2",
            "id":2
        }
    ]


##root endpoint 
@app.get('/')
def root():
    return {"message":"hey welcome to my api"}


##Endpoint to get all the posts 
@app.get('/posts')
def get_post():
    cursor.execute("SELECT * FROM POSTS")
    posts=cursor.fetchall()
    return {"data": posts}




##finding a post with given id
def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p



##Endpoint to get a post using post ID 
@app.get("/posts/{id}")
def get_posts(id:int):
    cursor.execute("select * from posts where id=%s",(id,))
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} not found in the databse")

    return {"post details":post}


##Endpoint to create a post -->3
@app.post('/create_posts',status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    #cursor.execute(f"INSERT INTO POSTS (title,content,published) VALUES({post.title},{post.content},{post.puiblished})")-->.this may voilate the sql injection if you type sql commands in the string (Bad practice)
    cursor.execute("INSERT INTO POSTS (title,content,published) VALUES(%s,%s,%s)",
                   (post.title,post.content,post.published))
    connection.commit()
    added_post_id=cursor.lastrowid
    cursor.execute("select * from posts where id=%s",(added_post_id,))
    added_post=cursor.fetchall()
    
    return {
            "message": "Post created successfully",
            'Data':added_post
            }
 

##function to get the product index use before database
def find_index(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i



##Endpoint to Delete a post with certain ID
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleting_post(id : int):
    cursor.execute("DELETE FROM POSTS WHERE ID=%s",(id,))
    count=cursor.rowcount  #-->tells how many rows got effected
    connection.commit()
    if count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)



#Endpoint to updata a post with certain ID
@app.put("/posts/{id}")
def update_post(id:int,post:Post):

    cursor.execute("UPDATE POSTS SET title=%s,content=%s WHERE ID=%s",(post.title,post.content,id,))
    count=cursor.rowcount
    connection.commit()
    if count==0: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} was not found")

    
    return {"message": "Post updated successfully"}



##Endpoint to test the database integration
##@app.get("/test-db")
##def test_db(db: Session = Depends(get_db)):
   ## return {"message": "Database session obtained"}





            






