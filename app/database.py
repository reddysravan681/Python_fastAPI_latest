from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings


from urllib.parse import quote_plus
from app.config import settings

DATABASE_URL = f"mysql+pymysql://{settings.database_username}:{quote_plus(settings.database_password)}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()


#creating dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()