'''database model for both sqlite and postgress'''

from app import config
from werkzeug.security import generate_password_hash,check_password_hash


db=config.db

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    hashed_password = db.Column(db.String(255))
    role=db.Column(db.Text)
    
    def __init__(self,name,email,password,role):
        self.name=name
        self.email=email
        self.hashed_password=generate_password_hash(password)
        self.role=role
        
    def check_password(self,password):
        return check_password_hash(self.hashed_password,password)
    
    def get_id(self):
        return (self.user_id)
    

