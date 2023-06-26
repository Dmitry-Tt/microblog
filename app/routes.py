from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Dmitry'}
    posts = [
        {
            'author': {'username': 'Lera'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Mark'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Sergey'},
            'body': 'Сегодня хорошая погода.'
        },
        {
            'author': {'username': 'Дарья'},
            'body': 'Я хочу шаурму ...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
