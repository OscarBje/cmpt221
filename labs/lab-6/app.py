"""app.py: render and route to webpages"""

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
     return render_template('signup.html')
    frstnm = request.form['First Name']
    lstnm = request.form['Last Name']
    email = request.form['Email']
    phnr = request.form['Phone Number']
    pswrd = request.form['Password']
    new_user = User(frstnm=frstnm, lstnm=lastnm, email=email, phnr=phnr, pswrd=pswrd)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('users'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/users')
def users():
    with app.app_context():
        # select users where the first name is Calista
        # stmt = select(User).where(User.FirstName == "Calista")

        # select all users
        stmt = select(User)
        all_users = db.session.execute(stmt)

        return render_template('users.html', users=all_users)
    
    return render_template('users.html')

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

