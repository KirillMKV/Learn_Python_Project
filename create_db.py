from server import create_app
from models import db

db.create_all(app=create_app())