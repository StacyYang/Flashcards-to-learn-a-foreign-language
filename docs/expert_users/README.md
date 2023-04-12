# Flashcards-to-learn-a-foreign-language
## Description: 
1. A website where users can learn a foreign language using flashcards with their friends or alone. 
2. Users need to register their accounts, once login in, there are two modes:
    Study mode: Users study using flashcards.
    Quize mode: User score, quiz time will be recorded.
    
## Features: 
1. **User Authentication:** Allow users to create an account if they do not already have one. Login requires users to provide their username and password before they can have access to certain features or information of our website. And logout after they finish studying.
2. **Learn by using Flashcards:** Allow users to learn a new language, including its vocabulary, grammar, and cultural knowledge using flashcards. 
3. **Notes Creation:** Allow users to wirte notes based on their needs.
4. **Take quiz:**  Allow users to take quizzes based on their desired language. The system tracks users' scores and dates of taking the quiz, and then displays them on a scoreboard.
5. **Scoreboard:** Displays users' scores on quizzes. Users can view their own scores as well as the whole ranking scoreboard.
6. **Admin account:** Allow administer to manage the website, including view/delete all user accounts, view/delete quiz questions, view/delete flashcards.


## Technologies involved:
1. **Frontend:** HTML, CSS, JavaScript
2. **Backend:** Flask/Jinja, Python, SQLite for Database

## Test user:
<li>username: tester
<li>password: 1234567

## Administer account:
<li>username: administer
<li>password: 1234567

## Database
Database is pre-populated, if batabase doesn't have enought questions or flashcards, can re-populate database again.<br>
Steps: 
       <li> uncomment this line of code "from . import populate_database"  in __init__.py </li>
       <li> Refresh the website </li>
       <li> Comment off the code "from . import populate_database"  in __init__.py</li>

## Setup & Install:
Make sure you have the latest version of Python installed

```bash
git clone <repo-url>
```

```bash
pip install -r docs/expert_users/requirements.txt
```

## How to check status of product
After building the product
Running the app
```bash
python dev/main.py
```
Go to http://127.0.0.1:5000

Then you will be taken to our home page and you can start interacting with the product

## How to check weekly progress of product
Navigate to commit history https://github.com/StacyYang/Flashcards-to-learn-a-foreign-language/commits/main

### See code changes
Click on the commit id will see code changes

### View past status
Click the <> button on the commit history page

### Functions that can be checked:
<li> Sign up for a new account
<li> Login with your account, go to "choose language and mode".
     option 1: choose language, choose "study" to view flashcards, you can also add notes as needed.
     option 2: choose language, choose "quiz" to take a quiz and view your quiz result.
<li> Go to "scoreboard", view total rank and personal rank.
<li> Login as administer, go to "dashboard" to review all user accounts, flashcards and quiz questions.
<li> Logout is also implemented.

