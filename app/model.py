'''database model for both sqlite and postgress'''

from app.dbsetup import db
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    hashed_password = db.Column(db.String(255))

    
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.hashed_password=generate_password_hash(password)

        
    def check_password(self,password):
        return check_password_hash(self.hashed_password,password)
    
    def get_id(self):
        return (self.user_id)
    

