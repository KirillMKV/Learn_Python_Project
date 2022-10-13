from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from config import db_password, db_username
#from config import db_password, db_username

engine = create_engine(f'postgresql://{db_username}:{db_password}@peanut.db.elephantsql.com:5432/{db_username}', pool_pre_ping=True)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

