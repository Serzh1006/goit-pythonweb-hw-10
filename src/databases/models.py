from sqlalchemy import Column, Integer, String, Date
from .connect import Base, engine


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    birthday = Column(Date, nullable=True)


Base.metadata.create_all(bind=engine)
