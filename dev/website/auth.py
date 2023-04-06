from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Quiz_M, Quiz_TF, Material, Score, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  ## means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import func, desc
from random import shuffle
from datetime import datetime, timedelta
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

        errors = []

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='error')
            errors.append('Username already exists')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
            errors.append('Username must be greater than 1 character.')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
            errors.append('Password don\'t match.')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
            errors.append('Password must be at least 7 characters.')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            errors.append('Email must be greater than 3 characters.')
        else:
            # add user to database
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # user will automatically logined after signup
            login_user(new_user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('auth.choose_lang_mode'))

    return render_template("login.html", user=current_user, active_tab='tab-2')


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
            return redirect(url_for('auth.take_quiz', user=current_user, language=language))

        elif mode == 'study':
            return redirect(url_for('auth.study', language=language, user=current_user))

    return render_template("choose_lang_mode.html", user=current_user)


@auth.route('/study', methods=['GET', 'POST'])
@login_required
def study():
    # Get the language from the URL parameter
    language = request.args.get('language', 'Chinese')

    # The number of chapters
    num_chapter = 5
    # The number of cards in one chapter
    num_card_chapter = 20

    # Select 9 random Material from the database
    allCards = Material.query.filter_by(language=language).order_by(
        func.random()).limit(num_chapter * num_card_chapter).all()
    shuffle(allCards)
    res_cards = {i: [] for i in range(1, num_chapter + 1)}

    # Arrange to chapter
    for i in range(1, num_chapter + 1):
        for _ in range(num_card_chapter):
            res_cards[i].append(allCards.pop())

    allNotes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date.desc()).all()
    for note in allNotes:
        # chagne timezone
        tz_delta = timedelta(hours=-7)
        note.date += tz_delta

    return render_template('study.html', user=current_user, cards=res_cards, notes=allNotes, language=language)


@auth.route('/addnote/<string:content>', methods=['GET'])
@login_required
def add_note(content):
    print(current_user.username)
    all_note = Note.query.filter_by(user_id=current_user.id).order_by(Note.id.desc()).all()
    new_note_id = None
    if len(all_note) == 0:
        new_note_id = 1
    else:
        new_note_id = all_note[0].id + 1

    db.session.add(Note(data=content, date=func.now(), user_id=current_user.id))

    db.session.commit()
    print(str(new_note_id))
    return str(new_note_id)


@auth.route('/delete_note/<string:id>', methods=['GET'])
@login_required
def delete_note(id):
    if not id.startswith("note-"):
        return "error"
    try:
        id = int(id.split("-")[1])
    except:
        return "error"
    all_note = Note.query.filter_by(id=id).all()
    if len(all_note) != 1:
        return "error"
    db.session.delete(all_note[0])
    db.session.commit()
    return "success"


@auth.route('/update_note/<string:id>/<string:note_content>', methods=['GET'])
@login_required
def update_note(id, note_content):
    if not id.startswith("note-"):
        return "error"
    try:
        id = int(id.split("-")[1])
    except:
        return "error"
    all_note = Note.query.filter_by(id=id).all()
    if len(all_note) != 1:
        return "error"

    Note.query.filter_by(id=id).update({'data': note_content, 'date': func.now()})
    db.session.commit()
    return "success"


# for cache quiz
__user_quizzes_multi = {}
__user_quizzes_tf = {}


@auth.route('/quiz_take', methods=['GET', 'POST'])
@login_required
def take_quiz():
    # Get the language from the URL parameter
    language = request.args.get('language', 'Chinese')

    # Select 10 random quiz questions from the database
    # Use the chosen language to filter the quiz questions using the filter_by() method.
    quizzes_multi = Quiz_M.query.filter_by(language=language).order_by(func.random()).limit(5).all()
    quizzes_tf = Quiz_TF.query.filter_by(language=language).order_by(func.random()).limit(5).all()

    total = 10 * len(quizzes_multi + quizzes_tf)

    if request.method == 'POST':
        # Initialize the a list of dictionaries. 
        quiz_list = []
        user_answers = request.form
        score = 0

        for key, value in user_answers.items():
            # print(key, value)
            if key.startswith('answer-'):
                quiz_id = key.split('-')[1]
                # print(quiz_id)  # quiz id in database
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
            quiz_list.append(
                {"question_text": question_text, "user_answer": user_answer, "correct_answer": correct_answer})

        # Display the score, correct answer and user's answers.
        if len(user_answers) == 0:
            flash('You did not answer any questions, please take the quiz')
            return redirect(url_for('auth.take_quiz', user=current_user, language=language))
        else:
            # Save user score and date to database
            quiz_score = Score(user_id=current_user.id, score=score, date=datetime.now())
            db.session.add(quiz_score)
            db.session.commit()
            return render_template('quiz_result.html', user=current_user, language=language, quiz_list=quiz_list,
                                   score=score, total=total)

    # If it's a GET request, display the quiz questions
    return render_template('quiz_take.html', user=current_user, language=language, quizzes_multi=quizzes_multi,
                           quizzes_tf=quizzes_tf)


# Administer related routes
@auth.route('/administer_login', methods=['GET', 'POST'])
def administer_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and username != "administer":
            flash('This is the administer login. Please login as a regular user.', category='error')
            return render_template("login.html", user=current_user)
        elif user and username == "administer":
            if check_password_hash(user.password, password):
                flash('Logged in successfully as the administer!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.admin_dashboard', user=current_user))
            else:
                flash('Incorrect password, try again.', category='error')
                return render_template("login.html", active_tab='tab-3', user=current_user)
        else:
            flash('User does not exists. Please try again.', category='error')
            return render_template("login.html", active_tab='tab-3', user=current_user)

    return render_template("login.html", user=current_user)


@auth.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if current_user.username == 'administer':
        users = User.query.all()
        quiz_m = Quiz_M.query.all()
        quiz_tf = Quiz_TF.query.all()
        flashcards = Material.query.all()

        # Set default active tab to be user accounts
        tab = request.args.get('tab', 'user-accounts')

        return render_template('admin_dashboard.html', users=users, user=current_user, quiz_m=quiz_m, quiz_tf=quiz_tf,
                               flashcards=flashcards, tab=tab)
    else:
        return render_template("login.html", user=current_user)


@auth.route('/admin/users/delete/<int:user_id>', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    if current_user.username == 'administer' and request.method == 'POST':
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('auth.admin_dashboard'))
    else:
        return render_template("login.html", user=current_user)


@auth.route('/admin/mcq/delete/<int:question_id>', methods=['POST'])
@login_required
def admin_delete_multi_question(question_id):
    if current_user.username == 'administer' and request.method == 'POST':
        question = Quiz_M.query.get(question_id)
        if question:
            db.session.delete(question)
            db.session.commit()

        tab = request.args.get('tab', 'multiple-choice-quiz')
        return redirect(url_for('auth.admin_dashboard', _anchor=tab, tab=tab))
    else:
        return render_template("login.html", user=current_user)


@auth.route('/admin/tf/delete/<int:question_id>', methods=['POST'])
@login_required
def admin_delete_tf_question(question_id):
    if current_user.username == 'administer' and request.method == 'POST':
        question = Quiz_TF.query.get(question_id)
        if question:
            db.session.delete(question)
            db.session.commit()

        tab = request.args.get('tab', 'true-or-false-quiz')
        return redirect(url_for('auth.admin_dashboard', _anchor=tab, tab=tab))
    else:
        return render_template("login.html", user=current_user)


@auth.route('/admin/flashcard/delete/<int:flashcard_id>', methods=['POST'])
@login_required
def admin_delete_flashcard(flashcard_id):
    if current_user.username == 'administer' and request.method == 'POST':
        flashcard = Material.query.get(flashcard_id)
        if flashcard:
            db.session.delete(flashcard)
            db.session.commit()

        tab = request.args.get('tab', 'flashcards')
        return redirect(url_for('auth.admin_dashboard', _anchor=tab, tab=tab))
    else:
        return render_template("login.html", user=current_user)


@auth.route('/scoreboard', methods=['GET'])
@login_required
def scoreboard():
    # model to templatem, ready to fill in.
    user_score = {"username": current_user.username, "rank": "None",
                  "total_score": "None", "newest_score": "None", "newest_time": "None"}
    all_rows = []
    rank_table = db.session.query(Score.user_id, func.sum(Score.score).label(
        "total_score")).group_by(Score.user_id).order_by(desc("total_score")).all()
    for rank, item in enumerate(rank_table):
        try:
            user = User.query.filter_by(id=item[0]).one()
        except:
            continue
        user_score_newest = Score.query.filter_by(
            user_id=user.id).order_by(Score.date.desc()).first()
        row = {"username": user.username, "rank": rank + 1,
               "total_score": item[1], "newest_score": user_score_newest.score, "newest_time": user_score_newest.date}
        # replace user_score
        if item[0] == current_user.id:
            user_score = row
        all_rows.append(row)

    return render_template('scoreboard.html', user=current_user, user_score=user_score, all_score=all_rows)


@auth.route('/scoreboard/look', methods=['GET'])
@login_required
def scoreboard_user():
    # model to templatem, ready to fill in.
    all_score = []
    # user be looked
    user_looked = User.query.filter_by(username=request.args.get('username')).one()
    all_score = Score.query.filter_by(user_id=user_looked.id).order_by(Score.date.desc()).all()

    return render_template('scoreboard_user.html', user=current_user, user_looked=user_looked, all_score=all_score)
