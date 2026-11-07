
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus
from pathlib import Path

from app.config import settings

# Locate the Aiven CA certificate
CA_CERT_PATH = Path(__file__).resolve().parent.parent / "certs" / "ca.pem"

# Connect to hosted MySQL
DATABASE_URL = (
    f"mysql+pymysql://{settings.database_username}:"
    f"{quote_plus(settings.database_password)}@"
    f"{settings.database_hostname}:"
    f"{settings.database_port}/"
    f"{settings.database_name}"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {
            "ca": str(CA_CERT_PATH)
        }
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
