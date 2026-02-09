from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapi_db"

# DATABASE_URL = F"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}:{MYSQL_HOST}:{MYSQL_PORT}:{MYSQL_DATABASE}"


DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/fastapi_db"

# Connection
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

# Base
Base = declarative_base()          