'''Config file with for all database connection'''

import os
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from app import app


####################################


db=SQLAlchemy(app) #to connect database with ORM


#basic configuration
class config():
    SQLALCHEMY_DATABASE_URI=None
    SQLALCHEMY_TRACK_MODIFICATIONS= False



#Configuratuon for sqlite
class sqliteconfig(config):
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'testdata.sqlite3')



#configuration for postgresql
class postgresconfiig(config):
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:kv79@localhost:5432/testdata'


#configuration for mongodb
class mongodbconfig(config):
    client = MongoClient('mongodb://localhost:27017')
    db = client['test']
    collection = db['users']