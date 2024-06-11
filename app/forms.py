
'''Basic registration and login form'''

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo,Length

######################################################

class Usersregistration(FlaskForm):
    name=StringField('Enter your name: ',validators=[DataRequired()])
    email=StringField('Enter your email: ',validators=[DataRequired(),Email()],render_kw={'placeholder':'abc@xyzmail.com'})
    password=PasswordField('Password: ',validators=[DataRequired(),Length(min=8),EqualTo('pass_confirm',message='Passwords must match')],render_kw={'placeholder':'Min 8 charcters'})
    pass_confirm=PasswordField('Confirm password: ',validators=[DataRequired()])
    register=SubmitField('Register')

####################################################    

class Userslogin(FlaskForm):
    email=StringField('Enter your registered email: ',validators=[DataRequired(),Email()])
    password=PasswordField('Enter your password: ',validators=[DataRequired()])
    login=SubmitField('Log in')
    

