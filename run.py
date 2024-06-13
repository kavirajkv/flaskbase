
from flask import Flask
from app import config
# from app.dbsetup import db
from app.config import sqliteconfig, postgresconfig,config

######################################

app=None

def create_app():
    app=Flask(__name__,template_folder="./app/templates")
    app.config.from_object(config)
    # app.config.from_object(sqliteconfig)
    # db.init_app(app)
# 
    app.app_context().push()

    # with app.app_context():
        # db.create_all()

    return app
    
app=create_app()

from app.view import *


if __name__=="__main__":
    app.run(debug=True)