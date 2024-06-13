
# from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient


# db = SQLAlchemy()

client = MongoClient('mongodb://localhost:27017')
mongo = client['kavi']
collection = mongo['users']