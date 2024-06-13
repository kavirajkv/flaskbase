'''Config file with for all database connection'''

import os




####################################



# basic configuration
class config():
    SQLALCHEMY_DATABASE_URI=None
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY='secretkey'


# Configuratuon for sqlite
class sqliteconfig(config):
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'testdata.sqlite3')



# configuration for postgresql
class postgresconfig(config):
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:postgres@localhost:5432/testdata'





