from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolen="True")

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password1 = request.form.get('password1').strip()
        password2 = request.form.get('password2').strip()
        email = request.form.get('email').strip()

        if len(username) < 2:
            flash('Username must be greater than 1 charachter.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 charachters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 charachters.', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
            
    return render_template("login.html", boolen="True")