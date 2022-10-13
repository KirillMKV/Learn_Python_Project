from sqlalchemy import Column, Integer, String, Date, Identity
from create_db import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,  primary_key=True, autoincrement=True, )
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    registration_date = Column(Date)

