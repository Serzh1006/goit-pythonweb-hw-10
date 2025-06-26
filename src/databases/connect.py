from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:111111@localhost:5432/contacts_db"

engine = create_engine(url=DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    connection = Session()
    try:
        yield connection
    finally:
        connection.close()
