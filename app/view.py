################################3
'''Basic views for an application'''

from flask import render_template,redirect,url_for,current_app as app
from app.forms import Usersregistration
from app.model import Users
from app.dbsetup import db

########################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form=Usersregistration()
    if form.validate_on_submit():
        user=Users(name=form.name.data,
                  email=form.email.data,
                  password=form.password.data,
                  )
        
        with app.app_context():
            checkuser=Users.query.filter_by(email=form.email.data).first()
            if checkuser:
                return redirect(url_for('index'))
            else:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('sucess'))
    return render_template('register.html',form=form)
                

@app.route('/sucessupdate')
def sucess():
    return render_template('sucess.html')