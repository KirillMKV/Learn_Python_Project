from create_db import db_session
from models import User

user = User(username='Fred')
db_session.add(user)
db_session.commit()