from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolen="True")

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>sign-up<p>"