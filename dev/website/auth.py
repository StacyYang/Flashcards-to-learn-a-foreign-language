from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Quiz_M, Quiz_TF, Material, Score
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ## means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import func
from random import shuffle
from datetime import datetime
from flask import abort




auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.choose_lang_mode'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email = request.form.get('email')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        else:
            # add user to database
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # user will automatically logined after signup
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            
            return redirect(url_for('auth.choose_lang_mode'))
            
    return render_template("login.html", user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/choose_lang_mode', methods=['GET', 'POST'])
@login_required
def choose_lang_mode():
    if request.method == 'POST':
        language = request.form['language']
        mode = request.form['mode']

        if mode == 'quiz':
            return redirect(url_for('auth.take_quiz',  user=current_user, language=language))

        elif mode == 'study':
            return redirect(url_for('auth.study', language=language, user=current_user))
    
    return render_template("choose_lang_mode.html", user=current_user)



@auth.route('/study', methods=['GET', 'POST'])
def study():
    # Get the language from the URL parameter
    language = request.args.get('language', 'Chinese')

    # Select 9 random Material from the database
    cards = Material.query.filter_by(language=language).order_by(func.random()).limit(9).all()
    shuffle(cards)
    return render_template('study.html', user=current_user,cards=cards, language=language)




@auth.route('/quiz_take', methods=['GET', 'POST'])
@login_required
def take_quiz():
    # Get the language from the URL parameter
    language = request.args.get('language', 'Chinese')

    # Select 10 random quiz questions from the database
    # Use the chosen language to filter the quiz questions using the filter_by() method.
    quizzes_multi= Quiz_M.query.filter_by(language=language).order_by(func.random()).limit(5).all()
    quizzes_tf= Quiz_TF.query.filter_by(language=language).order_by(func.random()).limit(5).all()


    if request.method == 'POST':
        # Initialize the a list of dictionaries. 
        quiz_list = []
        user_answers = request.form
        score = 0

        for key, value in user_answers.items():
            #print(key, value)
            if key.startswith('answer-'):
                quiz_id = key.split('-')[1]
                #print(quiz_id)  # quiz id in database
                if key.endswith('multi'):
                    question = Quiz_M.query.filter_by(id=quiz_id).first()
                    question_text = question.question
                    user_answer = question.get_option_string(int(value)) if value else "No answer provided"
                    correct_answer = question.get_answer_string()
                    if user_answer == correct_answer:
                        score += 10
                if key.endswith('tf'):
                    question = Quiz_TF.query.filter_by(id=quiz_id).first()
                    question_text = question.question
                    user_answer = question.get_option_string(int(value)) if value else "No answer provided"
                    correct_answer = question.get_answer_string()
                    if user_answer == correct_answer:
                        score += 10

            # Add question_text, user_answer and correct_answer to the list.
            # We are saving question_text, user_answer and correct_answer into this list, 
            # so that quiz_result.html can retrive info from it without querying database.
            quiz_list.append({"question_text": question_text, "user_answer": user_answer, "correct_answer": correct_answer})


        # Display the score, correct answer and user's answers.   
        if len(user_answers) == 0:
            flash('You did not answer any questions, please take the quiz')
            return redirect(url_for('auth.take_quiz', user=current_user, language=language))
        else:
            # Save user score and date to database
            quiz_score = Score(user_id=current_user.id, score=score, date=datetime.now())
            db.session.add(quiz_score)
            db.session.commit()
            return render_template('quiz_result.html', user=current_user, language=language, total=100, quiz_list=quiz_list, score=score)
   
    # If it's a GET request, display the quiz questions
    return render_template('quiz_take.html', user=current_user, language=language, quizzes_multi=quizzes_multi, quizzes_tf=quizzes_tf)


   

# Administer related routes
@auth.route('/administer_login', methods=['GET', 'POST'])
def administer_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully as the administer!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.admin_dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('This is the administer login.', category='error')

    return render_template("login.html", user=current_user)
       

@auth.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if current_user.username == 'administer':
        users = User.query.all()
        quiz_m = Quiz_M.query.all()
        return render_template('admin_dashboard.html', users=users, user=current_user, quiz_m=quiz_m)
    else:
        abort(403)
    
    


@auth.route('/admin/users/delete/<int:user_id>', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    if current_user.username == 'administer'  and request.method == 'POST' :
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('auth.admin_dashboard'))
    else:
        abort(403)
    
   
   


