from fastapi import FastAPI,Depends
from app.database import engine,get_db
from app import models
from sqlalchemy.orm import Session
from app.routers import posts,users,auth,vote
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware




#models.Base.metadata.create_all(bind=engine)
origins=['*']
#creating the object of fastAPI
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


##root endpoint 
@app.get('/')
def root():
    return {"message":"hey welcome to my fastAPI"}


##Endpoint to test the database integration
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    #posts.mappings().all()-->fails
    return {"posts":posts}


##Registering the routs in routers in 
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


            






